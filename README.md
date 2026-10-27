# CodeAlpha Data Redundancy Removal System

A beginner-friendly web application developed for the CodeAlpha Cloud Computing Internship — Task 1.

## Project Overview

This application helps prevent duplicate records from being stored in a database. Users can submit a person's name, email address, and phone number. The system validates the information and checks whether the email address already exists before saving the record.

## Features

- Add new records through a web form.
- Validate required fields.
- Check basic email address format.
- Detect duplicate email addresses without case sensitivity.
- Store unique records using SQLite.
- Display saved records in a table.
- Show the total number of saved records.

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- Git and GitHub

## Installation and Setup

1. Install Python.
2. Open a terminal in the project folder.
3. Create a virtual environment:

   ```powershell
   py -m venv .venv
   ```

4. Activate the environment:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

5. Install the dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

6. Start the application:

   ```powershell
   python app.py
   ```

7. Open http://127.0.0.1:5000 in your browser.

## Testing

1. Add a record using a new email address.
2. Submit the same email address again using different capitalization.
3. Confirm that the application rejects the duplicate.
4. Try an invalid email address or leave a required field empty.
5. Confirm that the validation messages appear.

## Project Limitation

The system uses the email address as the unique identifier. It does not determine whether different email addresses belong to the same person, and basic format validation does not prove that an email inbox exists.

## Security Note

Use fictional information for testing. This educational project is not intended for confidential personal information.

## Author

Developed as a CodeAlpha Cloud Computing Internship project.
