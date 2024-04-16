-- CREATE DATABASE PlumbingShop_DB;

-- USE PlumbingShop_DB;

-- CREATE TABLE HumanResource(
-- HR_ID INT PRIMARY KEY,
-- StaffNumber INT,
-- JobDescription VARCHAR(255)
-- );

-- CREATE TABLE Interns(
-- Intern_ID INT,
-- PhoneNumber VARCHAR(15),
-- JobDescription VARCHAR(255)
-- );

-- making a column have a primary key 
-- ALTER TABLE Interns
-- Intern_ID PRIMARY KEY;

-- Removing primary key from a column
-- ALTER TABLE Interns
-- DROP PRIMARY KEY;

-- ALTER TABLE Interns
-- ADD CONSTRAINT FK_HR_ID
-- FOREIGN KEY (Intern_ID)
-- REFERENCES HumanResource(HR_ID);

-- Removing Foreign key
-- ALTER TABLE Interns
-- DROP CONSTRAINT FK_HR_ID;

-- unique constraint
-- CREATE TABLE Tools(
-- ToolsID INT,
-- TName VARCHAR(255) UNIQUE,
-- TPrice VARCHAR(255)
-- );

-- Adding unique constraint
-- ALTER TABLE Interns
-- ADD CONSTRAINT UQ_PhoneNumber UNIQUE(PhoneNumber);

-- Removing unique constraint
-- ALTER TABLE Interns
-- DROP CONSTRAINT UQ_PhoneNumber UNIQUE(PhoneNumber);

-- Adding NOT NULL constraint
-- ALTER TABLE Tools
-- MODIFY TPrice VARCHAR(255) NOT NULL;

-- Removing NOT NULL constraint
-- ALTER TABLE Tools
-- MODIFY TPrice VARCHAR(255); -- you won't specify the constraint