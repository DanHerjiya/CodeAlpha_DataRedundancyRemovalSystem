import os
import re
import sqlite3
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-for-production")

# Locally, the database is created in this project's folder.
# On a hosting service, set DATABASE_PATH to a persistent storage location if available.
DATABASE_PATH = os.environ.get(
    "DATABASE_PATH",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "records.db")
)


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL COLLATE NOCASE UNIQUE,
                phone TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        connection.commit()


def valid_email(email):
    # A simple beginner-friendly format check, not a guarantee that an address exists.
    return re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email) is not None


initialize_database()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        phone = request.form.get("phone", "").strip()

        if not name or not email or not phone:
            flash("Please fill in all three fields.", "error")
            return redirect(url_for("index"))

        if not valid_email(email):
            flash("Please enter an email address in a valid format.", "error")
            return redirect(url_for("index"))

        digits_only = re.sub(r"\D", "", phone)
        if len(digits_only) < 7:
            flash("Please enter a phone number containing at least 7 digits.", "error")
            return redirect(url_for("index"))

        try:
            with get_connection() as connection:
                connection.execute(
                    "INSERT INTO records (name, email, phone) VALUES (?, ?, ?)",
                    (name, email, phone)
                )
                connection.commit()
            flash("Record saved successfully. This email was not already in the database.", "success")
        except sqlite3.IntegrityError:
            flash("Duplicate detected: this email address is already registered. No new record was saved.", "error")

        return redirect(url_for("index"))

    with get_connection() as connection:
        records = connection.execute(
            "SELECT id, name, email, phone, created_at FROM records ORDER BY id DESC"
        ).fetchall()
        total_records = connection.execute("SELECT COUNT(*) FROM records").fetchone()[0]

    return render_template("index.html", records=records, total_records=total_records)


if __name__ == "__main__":
    # Debug mode is useful locally; the production hosting service runs the app differently.
    app.run(debug=True)
