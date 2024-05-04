CREATE DATABASE suitandtie;

USE suitandtie;

CREATE TABLE employee(
	id INT PRIMARY KEY,
	first_name VARCHAR(225),
    last_name VARCHAR(225),
    job_title VARCHAR(225),
    salary DECIMAL(10, 2)
);

CREATE TABLE employee_archive(
	id INT PRIMARY KEY,
	first_name VARCHAR(225),
    last_name VARCHAR(225),
    job_title VARCHAR(225),
    salary DECIMAL(10, 2),
    archive_at TIMESTAMP EDEFAULT CURRENT_TIMESTAMP
);

INSERT INTO employee(id, first_name, last_name, job_title, salary)
VALUES
(1, 'Gerald', 'Macherechedze', 'Database Engineer', 20.50),
(2, 'Juliet', 'Mas', 'Database Admin', 20.50),
(3, 'Brain', 'Macherechedze', 'Database Engineer', 25.50),
(4, 'Nelson', 'Macherechedze', 'Software Engineer', 30.50),
(5, 'Nsuku', 'Macherechedze', 'Data Analyst', 40.50),
(5, 'Thabo', 'Macherechedze', 'Digital marketer', 35.50),
(6, 'Solomon', 'Macherechedze', 'Database Engineer', 210.50);

INSERT INTO employee_archive(id, first_name, last_name, job_title, salary)
VALUES
(1, 'Gerald', 'Macherechedze', 'Database Engineer', 20.50),
(2, 'Juliet', 'Mas', 'Database Admin', 20.50),
(3, 'Brain', 'Macherechedze', 'Database Engineer', 25.50),
(4, 'Nelson', 'Macherechedze', 'Software Engineer', 30.50),
(5, 'Nsuku', 'Macherechedze', 'Data Analyst', 40.50),
(5, 'Thabo', 'Macherechedze', 'Digital marketer', 35.50),
(6, 'Solomon', 'Macherechedze', 'Database Engineer', 210.50);

CREATE TABLE backup(
	id INT PRIMARY KEY,
	first_name VARCHAR(225),
    last_name VARCHAR(225),
    job_title VARCHAR(225),
    salary DECIMAL(10, 2)
);

-- copying data
INSERT INTO backup (id, first_name, last_name, job_title, salary)
SELECT id, first_name, last_name, job_title, salary
FROM employee
WHERE job_title = 'Database Admin';

SELECT * FROM backup;

-- delete one or more rows:
DELETE FROM backup
WHERE id = 8;
-- if WHERE condition is not specified, all rows will be deleted

-- cascade delete constraint. you need to have a foreign key - for a relationship
ALTER TABLE employee_archive
ADD CONSTRAINT 
fk_employee_archive
FOREIGN KEY (employee_id)
REFERENCES employee(id)
ON DELETE CASCADE;