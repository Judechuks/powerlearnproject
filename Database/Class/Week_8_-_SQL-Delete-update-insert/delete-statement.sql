/*
The SQL DELETE statement is used to remove one or more records from a table in a database. It allows you to delete specific rows based on a condition or delete all rows if no condition is specified.

SYNTAX:
DELETE FROM table_name
WHERE condition;

1. SQL DELETE 1 Row in a Table:
To delete a single row from a table, you can use the 'DELETE' statement with a condition that uniquely identifies the row to be deleted. Here's an example:

DELETE FROM employees
WHERE employee_id = 102;

2. SQL DELETE Multiple Rows in a Table:
To delete multiple rows from a table, broaden the WHERE clause to include the conditions for the desired rows. For instance:

DELETE FROM employees
WHERE status = 'Inactive'

3. SQL DELETE Rows from Related Tables:
When dealing with related tables (tables with foreign key relationships), deleting rows requires special consideration to maintain data integrity. If foreign key constraints are defined, you may need to delete rows from related tables first or handle the deletion through cascading actions.

DELETE FROM customers
WHERE customer_id = 101;
*/