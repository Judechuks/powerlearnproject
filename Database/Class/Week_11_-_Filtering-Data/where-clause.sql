/*
To select a specific row from a table, you use the WHERE clause in the SE:LECT statement
*/
SELECT column1, column2, ...
FROM table_name 
WHERE condition;

/*
💡The WHERE clause appears immediately after the FROM clause. The WHERE clause contains one or more logical expressions that evaluate each row in the table. If a row that causes the condition evaluates to true, it will be included in the result set; otherwise, it will be excluded.

💡Note that SQL has three-valued logic which are TRUE, FALSE, and UNKNOWN. It means that if a row causes the condition to evaluate to FALSE or NULL, the row will not be returned.

💡Note the the logical expression that follows the WHERE clause is also know as a predicate. You can use various operators to form the row selection criteria used in the WHERE clause.

💡operators; = equal to, <> or != not equal to, < less than, > greater than, <= less than or equal to, >= greater than or equal to

Besides the SELECT statement, you can use the WHERE claus ein the UPDATE or DELETE statement to specify which row to be updated or deleted.
*/

-- The following query finds employees who have salaries greater than 14,000 and sorts the result set based on the salary in the descending order.
SELECT employee_id, first_name, last_name, salary
FROM employees WHERE salary > 14000 
ORDER BY salary DESC;

-- SQL is case-insensitive. However, when it comes to the values in the comparisons, it is case-sensitive.
-- WHERE name = "Chen" is not the same as WHERE name = "CHEN"

-- SQL with date examples
SELECT employee_id, first_name, last_name, hire_date
FROM employees WHERE hire_date >= '1999-01-01' -- date is in YEAR-MONTH-DAY format 
ORDER BY hire_date DESC;

-- getting employees who joined the company in 1999
SELECT employee_id, first_name, last_name, hire_date
FROM employees WHERE YEAR(hire_date) = 1999 
ORDER BY hire_date DESC;

-- NOte that equal to operator can not be used to compare NULL values. The intension of the following query is to find all employees who do not have phone numbers:
SELECT employee_id, first_name, last_name, phone_number
FROM employees WHERE phone_number = NULL
-- However, it returns an empty result set because the following expression always return false. phone_number = NULL. To compare NULL values, you use IS NULL opeartor instead.
SELECT employee_id, first_name, last_name, phone_number
FROM employees WHERE phone_number IS NULL

/*
You can use the AND operator to combine two expressions.
WHERE department_id <> 8 AND department_id <> 9;
Interpreted as where department_id is not equal to 8 and department_id is not equal to 9
*/