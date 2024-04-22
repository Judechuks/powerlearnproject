/*
PLP - Software Development
Database Module
Week 5 Task
Create a new table in your database to store information about students. The table should have the following fields:
Student ID INT (Primary Key)
First Name
Last Name
Date of Birth
Email
Major
*/

-- CREATE DATABASE StudentsDB;

-- USE StudentsDB;

-- CREATE TABLE Students(
-- StudentID INT PRIMARY KEY, 
-- First_Name VARCHAR(25), 
-- Last_Name VARCHAR(25), 
-- Date_of_Birth DATE,
-- Email VARCHAR(255),
-- Major VARCHAR(255)
-- );

-- INSERT INTO Students(StudentID, First_Name, Last_Name, Date_of_Birth, Email, Major)
-- VALUES
-- ('1001', 'Jude', 'Monye', '1998-4-20', 'judemonye3020@gmail.com', 'Computer Science'),
-- ('1002', 'Judith', 'Peters', '1997-9-26', 'judithpeters22@gmail.com', 'Animal Science'),
-- ('1003', 'James', 'Martins', '1996-6-22', 'jamesmartins20@gmail.com', 'Environmental Science');

SELECT * FROM Students;