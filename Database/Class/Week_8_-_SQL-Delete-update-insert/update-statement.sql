/*
The SQL UPDATE statement is used to modify existing records in a table. It allows you to change the values in one or more columns of a row or multiple rows based on a specified condition.

SYNTAX:
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;

1. Update 1 Row:
To update a single row in a table, you can use 'UPDATE' statement with a specific condition that identifies the row uniquely. For example:

UPDATE employees
SET salary = 60000
WHERE employee_id = 101;

2. Update Multiple Rows:
To update multiple rows in a table, broaden the 'WHERE' clause to include the conditions for the desired rows. For instance:

UPDATE employees
SET status = 'Active'
WHERE department = 'IT';
*/