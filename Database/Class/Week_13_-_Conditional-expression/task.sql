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
    (1, 'John', 'Doe', 60000.00, 0.10), -- 10% bonus
    (2, 'Jane', 'Smith', 75000.00, 0.15), -- 15% bonus
    (3, 'Alice', 'Johnson', 90000.00, 0.12), -- 12% bonus
    (4, 'Mary', 'Johnson', 72000.00, 0.08), -- 8% bonus
    (5, 'Robert', 'Brown', 55000.00, 0.12), -- 12% bonus
    (6, 'Emily', 'Lee', 68000.00, 0.09), -- 9% bonus
    (7, 'David', 'Miller', 80000.00, 0.15), -- 15% bonus
    (8, 'Sophia', 'Garcia', 62000.00, 0.11), -- 11% bonus
    (9, 'Daniel', 'Clark', 90000.00, 0.14), -- 14% bonus
    (10, 'Olivia', 'Hall', 75000.00, 0.10), -- 10% bonus
    (11, 'Michael', 'Smith', 58000.00, 0.07), -- 7% bonus
    (12, 'Emma', 'Wang', 71000.00, 0.13), -- 13% bonus
    (13, 'William', 'Adams', 67000.00, 0.10), -- 10% bonus
    (14, 'Philip', 'Mark', 68000.00, 0.13), -- 13% bonus
    (15, 'Stephanie', 'Shaw', 75000.00, 0.16); -- 16% bonus

-- Adding the TotalCompensation Column
ALTER TABLE Employees
ADD TotalCompensation DECIMAL(10, 2) GENERATED ALWAYS AS (
    Salary + (Salary * BonusPercentage)
) STORED;

-- Identifying Employees with Total Compensation > $80,000
SELECT *
FROM Employees
WHERE TotalCompensation > 80000.00;

-- Updating FirstName for Low Compensation Employees
UPDATE Employees
SET FirstName = 'LowCompensation'
WHERE TotalCompensation < 60000.00;

-- For the other version (CASE statement which the task actually specifies) visit the assignment folder