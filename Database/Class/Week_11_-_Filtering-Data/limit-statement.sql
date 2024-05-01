/*
To limit the number of rows that is returned from a SELECT statement, you use the LIMIT and OFFSET clause


SYNTAX FOR LIMIT and OFFSET statement:
SELECT column_list
FROM table_name
ORDER BY column_list
LIMIT column_count OFFSET offset;

The LIMIT row_count determines the number of rows (row_count) returned by the query.
The OFFSET offset clause skips the offset rows before beginning to return the rows.
The OFFSET clause is optional, if you omit it, the query will return the row_count rows from the first row returned by the SELECT clause. 
When you see the LIMIT clause, it is important to use the ORDER BY clause to ensure the order of rows in the result set.

Not all database systems supports the LIMIT clause, Therefore, the LIMIT clause is available in some database systems only such as MySQL, PostgreSQL, SQLite, SybaseSQL, Anywhere, and HSQLDB. If you use SQL Server, you can use SELECT TOP instead.

Example: The following statement returns all the rows in the employees table sorted by the first_name column.
*/

SELECT employee_id, first_name, last_name
FROM employees
ORDER BY first_name;

-- The following example uses the LIMIT clause to return the first 5 rows in the result set returned by SELECT clause:

SELECT employee_id, first_name, last_name
FROM employees
ORDER BY first_name
LIMIT 5;

-- The following example uses both the LIMIT and OFFSET clauses to return the 5 rows starting from the 4th row:

SELECT employee_id, first_name, last_name
FROM employees
ORDER BY first_name
LIMIT 5 OFFSET 3;

-- In MySQL, you can use the shorter form of the LIMIT and OFFSET clauses like this:
SELECT employee_id, first_name, last_name
FROM employees ORDER BY first_name LIMIT 3, 5;

/*
Using SQL LIMIT to get the top N rows with the highest or lowest value. For example, the following statement gets the top five employees with the highest salaries.
*/
SELECT employee_id, first_name, last_name
FROM employees ORDER BY salary DESC LIMIT 5;

/*
Suppose you have 2 employees with the same salary and their salary is the highest and you want to get the person with the highest salary using LIMIT 1 OFFSET 1, this will only return 1 person. To fix this you can get the second(3rd, 4th,...) highest salary using these statements below:
*/
-- firstly:
SELECT DISTINCT salary FROM employees
ORDER BY salary DESC LIMIT 1, 1;

-- assuming the result = 17000
-- pass the result to another query:
SELECT employee_id, first_name, last_name, salary
FROM employees WHERE salary = 17000;

-- If you know subquery, you can combine both queries into a single query as follows:
SELECT employee_id, first_name, last_name, salary
FROM employees WHERE salary = (SELECT DISTINCT salary FROM employees
ORDER BY salary DESC LIMIT 1, 1);