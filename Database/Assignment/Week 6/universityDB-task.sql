/*
Name: Monye Jude Chukwuemeke
PLP - Software Development
Database Module
Week 6 Task
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

-- Adding a GPA column to the students table 
ALTER TABLE Students
ADD GPA DECIMAL(3,2);

-- populating the GPA column by StudentID
UPDATE students
SET GPA = 3.0
WHERE StudentID <= 1003;

UPDATE Students 
SET GPA = 3.5
WHERE StudentID > 1003; 

--  Renaming the Student table 
ALTER TABLE Students
RENAME TO EnrolledStudents;

-- Creating a Course table
CREATE TABLE Courses(
CourseID INT PRIMARY KEY,
CourseName VARCHAR(100),
Instructor VARCHAR(100),
Credits INT
);

-- Inserting values into the Course table
INSERT INTO Courses(CourseID, CourseName, Instructor, Credits)
VALUES
('101', 'Database Design', 'Gerald', '4' ),
('102', 'Entrepreneurship', 'Nelly Alili', '3' ),
('103', 'Software Engineering', 'Kamau Suzan', '4' ),
('104', 'Dart and Flutter', 'Allan Lenkaa', '3' ),
('105', 'Python Programming', 'Annebel', '3' ),
('106', 'Web Development', 'Gerald', '3' );

-- Deleting the EnrolledStudents table
DROP TABLE EnrolledStudents;

SELECT * FROM Courses