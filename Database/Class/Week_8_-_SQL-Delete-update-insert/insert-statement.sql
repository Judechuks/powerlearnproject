/*
In SQL, the INSERT statement is used to add new records or rows into a table.

SYNTAX:
# 1. Single row insertion
INSERT INTO tableName(column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

# 2. Multiple row insertion
INSERT INTO tableName(column1, column2, column3, ...)
VALUES (value1, value2, value3, ...),
       (value1, value2, value3, ...),
       (value1, value2, value3, ...);

# 3. Copying rows from other Tables:
INSERT INTO new_employees(first_name, last_name, job_title, salary)
SELECT first_name, last_name, job_title, salary
FROM old_employees
WHERE department = 'IT';
*/