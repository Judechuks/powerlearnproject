/*
Name: Monye Jude Chukwuemeke
PLP - Software Development
Database Module
Week 13 Task
Question:
Create a database with a table named Employees with columns EmployeeID, FirstName, LastName, Salary, and BonusPercentage. Populate the table with sample data. Write SQL queries to perform the following tasks:

1. Create a new column named TotalCompensation using the CASE statement, where Total Compensation is the sum of Salary and a bonus calculated based on the Bonus Percentage (e.g., if Bonus Percentage is 10, the bonus is 10% of the Salary).
2. Identify employees with a Total Compensation greater than $80,000.
3. Update the FirstName of employees with a Total Compensation less than $60,000 to 'LowCompensation'.
*/

-- Creating the SalesDB database
CREATE DATABASE IF NOT EXISTS SalesDB;

-- utilizing the SalesDB database
USE SalesDB;

-- Creating the Employees table
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Salary DECIMAL(10, 2) NOT NULL,
    BonusPercentage DECIMAL(5, 2) NOT NULL
);
-- BonusPercentage is the percentage of bonus (e.g., 10% = 0.10).

-- Populating the Table with Sample Data
INSERT INTO Employees (EmployeeID, FirstName, LastName, Salary, BonusPercentage)
VALUES
    (1, 'John', 'Doe', 60000.00, 10), -- 10% bonus
    (2, 'Jane', 'Smith', 75000.00, 15), -- 15% bonus
    (3, 'Alice', 'Johnson', 90000.00, 12), -- 12% bonus
    (4, 'Mary', 'Johnson', 72000.00, 8), -- 8% bonus
    (5, 'Robert', 'Brown', 55000.00, 12), -- 12% bonus
    (6, 'Emily', 'Lee', 38000.00, 9), -- 9% bonus
    (7, 'David', 'Miller', 80000.00, 15), -- 15% bonus
    (8, 'Sophia', 'Garcia', 62000.00, 11), -- 11% bonus
    (9, 'Daniel', 'Clark', 90000.00, 14), -- 14% bonus
    (10, 'Olivia', 'Hall', 75000.00, 10), -- 10% bonus
    (11, 'Michael', 'Smith', 58000.00, 7), -- 7% bonus
    (12, 'Emma', 'Wang', 71000.00, 13), -- 13% bonus
    (13, 'William', 'Adams', 67000.00, 10), -- 10% bonus
    (14, 'Philip', 'Mark', 68000.00, 13), -- 13% bonus
    (15, 'Stephanie', 'Shaw', 75000.00, 16); -- 16% bonus

-- Task 1: Adding the TotalCompensation Column and performing sum of salary and a bonus calculated based on the Bonus Percentage
ALTER TABLE Employees
ADD TotalCompensation DECIMAL(10, 2) GENERATED ALWAYS AS (
    Salary + (Salary * 
      CASE 
        WHEN BonusPercentage = 7 THEN 7/100
        WHEN BonusPercentage = 8 THEN 8/100
        WHEN BonusPercentage = 9 THEN 9/100 
        WHEN BonusPercentage = 10 THEN 10/100
        WHEN BonusPercentage = 11 THEN 11/100
        WHEN BonusPercentage = 12 THEN 12/100
        WHEN BonusPercentage = 13 THEN 13/100
        WHEN BonusPercentage = 14 THEN 14/100
        WHEN BonusPercentage = 15 THEN 15/100
        WHEN BonusPercentage = 16 THEN 16/100
        ELSE 0 -- Default bonus percentage (if not specified) 
      END
    )
) STORED;

-- viewing the columns of the the table
SELECT * FROM Employees;

-- Task 2: Identifying Employees with Total Compensation greather than $80,000
SELECT *
FROM Employees
WHERE TotalCompensation > 80000.00;

-- Task 3: Updating the FirstName of employees with a Total Compensation less than $60,000 to 'LowCompensation'.
-- UPDATE Employees
-- SET FirstName = 'LowCompensation'
-- WHERE TotalCompensation < 60000.00;

-- The above code does not work because of safe mode we can try this instead
SELECT EmployeeID FROM Employees WHERE TotalCompensation < 60000.00; -- the EmployeeID that match is 6
UPDATE Employees
SET FirstName = 'LowCompensation'
WHERE EmployeeID IN (6);

-- viewing the columns of the the table
SELECT * FROM Employees;