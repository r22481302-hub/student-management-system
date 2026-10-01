# Student Management System

A console-based Student Management System built using **Python and MySQL**. It allows users to add, view, search, update, and delete student records stored in a SQL database.

## Features

- Add student records
- View all students
- Search student by roll number
- Update student information
- Delete student records
- MySQL database storage
- Python MySQL database connectivity

## Tech Stack

- Python
- MySQL
- SQL
- mysql-connector-python

## Project Structure

```text
student-management-python-sql/
│
├── student_management.py
├── database.sql
├── requirements.txt
└── README.md
```

## How to Run

### 1. Install Python

Make sure Python is installed on your system.

### 2. Install MySQL

Install MySQL Server and create/configure your MySQL user.

### 3. Create the database

Open MySQL Workbench and run:

```sql
SOURCE path/to/database.sql;
```

Or copy and run the SQL commands from `database.sql`.

### 4. Install Python dependency

Open Command Prompt/Terminal in the project folder:

```bash
pip install -r requirements.txt
```

### 5. Configure MySQL password

Open `student_management.py` and replace:

```python
"password": "YOUR_MYSQL_PASSWORD"
```

with your actual MySQL password.

### 6. Run the project

```bash
python student_management.py
```

## Note

This is a learning project demonstrating Python CRUD operations with a MySQL database.
