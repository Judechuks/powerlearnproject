/*
Name: Monye Jude Chukwuemeke
PLP - Software Development
Database Module
Week 10 Task
*/

-- Creating the UniversityDB database
CREATE DATABASE UniversityDB;

-- utilizing the UniversityDB database
USE UniversityDB;

-- Creating the Students table
CREATE TABLE Students(
StudentID INT PRIMARY KEY, 
FirstName VARCHAR(50), 
LastName VARCHAR(50), 
Age INT,
Major VARCHAR(50)
);

-- Inserting data into the Students table 
INSERT INTO Students(StudentID, FirstName, LastName, Age, Major)
VALUES
('1001', 'Jude', 'Monye', '27', 'Computer Science'),
('1002', 'Judith', 'Peters', '19', 'Animal Science'),
('1003', 'Kelvin', 'Peterson', '20', 'Chemical Engineering'),
('1004', 'Prince', 'Bran', '26', 'Civil Engineering'),
('1005', 'Mary', 'Okoh', '24', 'Food Technology'),
('1006', 'Glory', 'Etim', '26', 'Statistics'),
('1007', 'James', 'Martins', '22', 'Environmental Science');

-- sorting students based on their age, to get the youngest student 
SELECT First_Name, Last_Name, Age
FROM Students
ORDER BY Age ASC;  
