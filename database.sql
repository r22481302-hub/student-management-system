CREATE DATABASE IF NOT EXISTS student_management;
USE student_management;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    roll_no VARCHAR(20) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    course VARCHAR(100) NOT NULL,
    semester INT NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(15)
);

-- Sample data
INSERT INTO students (roll_no, name, course, semester, email, phone)
VALUES
('101', 'Rahul Kumar', 'B.Tech CSE', 5, 'rahul@example.com', '9876543210'),
('102', 'Aman Singh', 'B.Tech CSE', 5, 'aman@example.com', '9876543211');
