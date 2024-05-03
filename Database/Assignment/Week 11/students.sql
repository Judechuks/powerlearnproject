/*
Name: Monye Jude Chukwuemeke
PLP - Software Development
Database Module
Week 11 Task
Question:
Create a database with a table named Students with columns StudentID, FirstName, LastName, Age, and Grade. 
Populate the table with sample data. Write SQL queries to perform the following tasks:
Retrieve all students who are older than 25 years.
Find students with a grade of 'A' or 'B' in the Grade column.
Display the distinct age values of students.
*/

-- creating the studentRecord database
CREATE DATABASE studentsRecord;

-- selecting the database to work on
USE studentsRecord;

-- creating the Students table
CREATE TABLE Students(
	StudentID INT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Age INT,
    Grade VARCHAR(2)
);

-- populating the Students table
INSERT INTO Students(StudentID, FirstName, LastName, Age, Grade)
VALUES
('1', 'Jude', 'Monye', '27', 'A'),
('2', 'Judith', 'Peters', '19', 'B'),
('3', 'Kelvin', 'Peterson', '20', 'B'),
('4', 'Prince', 'Bran', '26', 'B'),
('5', 'Mary', 'Okoh', '24', 'A'),
('6', 'Glory', 'Etim', '26', 'A'),
('7', 'James', 'Martins', '22', 'B');

-- task 1: retrieving all students who are older than 25
SELECT FirstName, LastName, Age
FROM Students WHERE Age > 25 
ORDER BY Age;

-- task 2: retrieving students with the grade of A or B in the Grade column
SELECT FirstName, LastName, Grade
FROM Students WHERE Grade = 'A' OR Grade = 'B'
ORDER BY Grade;

-- task 3: displaying the distinct age value of students
SELECT DISTINCT Age
FROM Students
ORDER BY Age;