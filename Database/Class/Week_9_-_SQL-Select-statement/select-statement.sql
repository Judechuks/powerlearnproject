/*
The SQL SELECT statement is used to retrieve data from one or more tables in a database. It is a fundamental query language command that allows you to specify the columns you want to retrieve and apply various conditions to filter the result set. The basic syntax of the SELECT statement is as follows:

SELECT column1, column2, ...
FROM table_name
WHERE condition;

Example: select all columns from the products table
SELECT * 
FROM products;

OPERATIONS THAT CAN BE DONE WITH SELECT STATEMENT
1. DISTINCT 
The SQL DISTINCT keyword serves to exclude duplicate rows from the result set obtained by a SELECT statement. When you use DISTINCT, it ensures that only unique values are returned for the specified columns. In other words, it retrieves only the first occurrence of each distinct row based on the specified columns.

For example, if you have a table with a column called “City” and you want to retrieve a list of unique cities, you can use the following query:

SELECT DISTINCT City FROM Customers;

This query will return a list of distinct city names from the Customers table, eliminating any duplicate entries.

Remember that DISTINCT operates on the entire row, not just a specific column.

2. ALIAS

SELECT column_name AS alias_name FROM table_name;

Here, column_name represents the actual name of the column you want to retrieve, and alias_name is the desired name you want to assign to that column in the result set. The AS keyword is optional but commonly used for clarity.

For example, if you have a table with a column named “Full_Name”, and you want to display it as “Name” in the result set, you can write:

SELECT Full_Name AS Name FROM Employees;
This query will return the Full_Name column from the Employees table, but it will be labeled as “Name” in the output

3. SORTING/ORDER
The SQL clause used to sort the result set in descending order is:

ORDER BY column_name DESC

In this syntax, replace column_name with the actual name of the column you want to sort. The DESC keyword specifies that the sorting should be done in descending order.
*/