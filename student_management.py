import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "YOUR_MYSQL_PASSWORD",
    "database": "student_management"
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    semester = int(input("Enter Semester: "))
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")

    conn = get_connection()
    cursor = conn.cursor()
    query = """INSERT INTO students
               (roll_no, name, course, semester, email, phone)
               VALUES (%s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, (roll, name, course, semester, email, phone))
    conn.commit()
    cursor.close()
    conn.close()
    print("Student added successfully.")

def view_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students ORDER BY roll_no")
    rows = cursor.fetchall()

    if not rows:
        print("No student records found.")
    else:
        print("\nID | Roll No | Name | Course | Semester | Email | Phone")
        print("-" * 85)
        for row in rows:
            print(row)

    cursor.close()
    conn.close()

def search_student():
    roll = input("Enter Roll No to search: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE roll_no = %s", (roll,))
    row = cursor.fetchone()

    if row:
        print("\nStudent Found:")
        print("ID:", row[0])
        print("Roll No:", row[1])
        print("Name:", row[2])
        print("Course:", row[3])
        print("Semester:", row[4])
        print("Email:", row[5])
        print("Phone:", row[6])
    else:
        print("Student not found.")

    cursor.close()
    conn.close()

def update_student():
    roll = input("Enter Roll No to update: ")
    name = input("Enter New Name: ")
    course = input("Enter New Course: ")
    semester = int(input("Enter New Semester: "))
    email = input("Enter New Email: ")
    phone = input("Enter New Phone: ")

    conn = get_connection()
    cursor = conn.cursor()
    query = """UPDATE students
               SET name=%s, course=%s, semester=%s, email=%s, phone=%s
               WHERE roll_no=%s"""
    cursor.execute(query, (name, course, semester, email, phone, roll))
    conn.commit()

    if cursor.rowcount:
        print("Student updated successfully.")
    else:
        print("Student not found.")

    cursor.close()
    conn.close()

def delete_student():
    roll = input("Enter Roll No to delete: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE roll_no = %s", (roll,))
    conn.commit()

    if cursor.rowcount:
        print("Student deleted successfully.")
    else:
        print("Student not found.")

    cursor.close()
    conn.close()

def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                add_student()
            elif choice == "2":
                view_students()
            elif choice == "3":
                search_student()
            elif choice == "4":
                update_student()
            elif choice == "5":
                delete_student()
            elif choice == "6":
                print("Program exited.")
                break
            else:
                print("Invalid choice.")
        except mysql.connector.Error as error:
            print("Database error:", error)
        except ValueError:
            print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()
