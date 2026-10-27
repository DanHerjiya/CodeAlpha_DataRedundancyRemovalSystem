# CodeAlpha - Data Redundancy Removal System

A beginner-friendly web application built for CodeAlpha Cloud Computing Task 1.

## Features

- Adds a record with a name, email address, and phone number.
- Checks that all fields are supplied.
- Performs a basic email-format check.
- Prevents duplicate email addresses (case-insensitive).
- Uses SQLite to store records.
- Displays saved records and the total count.
- Uses parameterized SQL queries.

## Technology

- Python
- Flask
- SQLite
- HTML and CSS
- Gunicorn for production hosting

## Run locally

1. Install Python 3.11 or a recent supported Python version.
2. Open a terminal in this project folder.
3. Create a virtual environment:

   Windows:
   ```powershell
   py -m venv .venv
   .venv\Scripts\activate
   ```

   macOS/Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```

5. Start the app:
   ```bash
   python app.py
   ```

6. Open http://127.0.0.1:5000 in your browser.

## Test the duplicate check

1. Add `Amina Yusuf`, `amina@example.com`, and `08012345678`.
2. Confirm that the record appears in the table and the count increases.
3. Try adding another record with `AMINA@example.com`.
4. The app should reject the second record because email comparison is case-insensitive.
5. Confirm that the count did not increase.
6. Try an invalid email or leave a field blank and confirm validation.

Use fictional data for testing. This project is a learning demo and is not intended to store confidential information.

## Cloud deployment notes

The included `Procfile` starts the app with Gunicorn on compatible hosting platforms. Set a strong `SECRET_KEY` environment variable in production. SQLite data may be lost on hosts with ephemeral filesystems after redeployment or restart. For persistent online data, configure a persistent disk and set `DATABASE_PATH` to a database file on that disk, or use a managed database. Check the selected host's current pricing and storage limits before deploying.

## Project scope and limitation

This project treats an email address as the unique identifier. It prevents duplicate email records but does not determine whether two different email addresses belong to the same person. The email-format check does not prove that the email inbox exists.
