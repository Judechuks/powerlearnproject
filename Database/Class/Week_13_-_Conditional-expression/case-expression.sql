/*
Conditional Expressions:
CASE Expression - add if-then-else logic to SQL statements

Introduction to SQL CASE expressions
The SQL CASE expression allows you to evaluate a list of conditions and returns one of the possible results. The CASE expression has two formats: simple CASE and searched CASE.

You can use the CASE expression in a clause or statement that allows a valid expression. For example, you can use the CASE expression in statements such as SELECT, DELETE, and UPDATE or in clauses such as SELECT, ORDER BY, and HAVING.

Simple CASE expression:
The following illustrates the simple CASE expression:

CASE expression
WHEN when_expression_l THEN
result_1
WHEN when_expression_2 THEN
result_2
WHEN when_expression_3 THEN
result_3
...
ELSE
else_result
END

The CASE expression compares an expression to a set of expression (when_expression_1, when_expression_2, when_expression_3, ...) using the equality operator (=). If you want to use other comparison operators such as greater than (>), less than (<), etc., you use the searched CASE expression.

The CASE statement returns the result_1, result_2, or result_3 if the expression matches the corresponding expression in the WHEN clause.

If the expression does not match any expression in the WHEN clause, it returns the else_result in ELSE clause. The ELSE clause is optional.

If you omit the ELSE clause and the expression does not match any expression in the WHEN clause, the CASE expression returns NULL.

Simple CASE expression example
Let’s take a look at the employees table.

employees table
employee_id
first_name
last_name
emal
phone_number
hire_date
job_id
salary
manager_{d
department_id

Suppose the current year is 2000.

We can use the simple CASE expression to get the work anniversaries of employees by using the following statement:

SELECT first_name, last_name, hire_date,
CASE (2000 - YEAR(hire_date))
  WHEN 1 THEN '1 year'
  WHEN 3 THEN '3 years’
  WHEN 5 THEN '5 years’
  WHEN 10 THEN '10 years'
  WHEN 15 THEN '15 years'
  WHEN 20 THEN '20 years'
  WHEN 25 THEN '25 years'
  WHEN 30 THEN '30 years'
  END aniversary
FROM employees
ORDER BY first_name;

The YEAR function returns the year when the employee joined the company. We get the number of years that the employee has been with the company and by subtracting the year when the employee joined the company from the current year (2000).

Then we compare the result with 1, 3, 5, 10, 15, 20, 25, 30 If the year of service equals one of these numbers, the CASE expression returns the work anniversary of the employee.

If the year of services of the employee does not match these numbers, the CASE expression returns NULL.

Searched CASE expression
The following shows the searched CASE expression.

CASE
WHEN boolean_expression_1 THEN
result_1
WHEN boolean_expression_2 THEN
result_2
WHEN boolean_expression_3 THEN
result_3
ELSE
else_result
END;

The database system evaluates the boolean expression for each WHEN clause in the order specified in the CASE expression.

If the Boolean expression in each WHEN clause evaluates to true, the searched CASE statement returns the result in the corresponding THEN clause.

If no Boolean expression returns true, the CASE expression return the else_result in the ELSE clause.

Like the simple CASE expression, the END clause is optional. If you omit the ELSE clause and
no Boolean expression evaluates to true, the CASE expression returns a NULL value.

Search CASE expression example
The following illustrates the searched CASE expression example.

SELECT first_name, last_name,
CASE
  WHEN salary < 3000 THEN 'Low'
  WHEN salary >= 3000 AND salary <= 5000 THEN 'Average'
  WHEN salary > 5000 THEN 'High'
END evaluation
FROM employees;

If the salary is less than 3000, the CASE expression returns “Low”. If the salary is between 3000 and 5000, it returns “average”. When the salary is greater than 5000, the CASE expression returns “High”.

In this tutorial, we have introduced you to the SQL CASE statement that allows you to add the IF THEN ELSE logic to the SQL statements.
*/