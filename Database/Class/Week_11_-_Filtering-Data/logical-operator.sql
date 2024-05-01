/*
SQL logical opeartors allows you to test for the truth of a condition. similar to a comparison operator, a logical operator returns a value of true, false, or unknown.

ALL - Returns true if all comparisons are true
AND - Returns true if both expressions are true
OR - Returns true if either expression is true
ANY - Returns true if any one of the comparisons is true
SOME - Returns true if some of the expressions are true
BETWEEN - Returns true if the operand is within a range
EXISTS - Returns true if any subquery contains any rows
IN - Returns true if the operand is equal to one of the value in a list
LIKE - Returns true if the operand matches a pattern
NOT - Reverses the result of any other boolean operator
*/
-- IS NULL operator compares a value with a NULL value and returns true if the compared value is NULL: otherwise, it returns false 

-- IS NOT NULL operator returns false if the compared value is NULL: otherwise, it returns true 

-- BETWEEN operator searches for values that are within a set of values, given the minimum value and maximum value. Note that the minimum and maximum values are included as part of the conditional set. 

SELECT employee_id, first_name, last_name, salary
FROM employees WHERE salary BETWEEN 9000 AND 12000
ORDER BY salary;

-- IN operator compares a value to a list of specified values. The IN operator returns true if the compared value matches at least one value in the list; otherwise, it returns false.
SELECT employee_id, first_name, last_name, department_id
FROM employees WHERE department_id IN (8,9)
ORDER BY department_id;

-- LIKE operator compares a value to similar values using a wildcard operator, SQL provides two wildcards used in conjunction with the LIKE operator:
-- The percent (%) represents zero, one, or multiple characters
-- The underscore sign (_) represents single character
SELECT employee_id, first_name, last_name
FROM employees WHERE first_name LIKE 'jo%'
ORDER BY first_name;
/*
Expressions => Meaning
LIKE 'Kim%' => matches a string that starts with Kim
LIKE '%er' => matches a string that ends with er
LIKE '%ch%' => matches a string that contains ch
LIKE 'Le_' => matches a string that starts with Le and is followed by one character e.g Len, Les, etc.
LIKE 'Jo__' => matches a string that starts with Le and is followed by at most two characters e.g John
LIKE '_uy' => matches a string that ends with uy and is preceded by one character e.g, guy
LIKE '%are_' => matches a string that contains 'are' and ends with one character
LIKE '_are%' => matches a string that contains 'are', starts with one character, and ends with any number of characters
-- NOTE: besides % and _ wildcards, some database systems may have other wildcards characters.

NOT LIKE - To negate the LIKE operator, you use the NOT operator.
*/
-- Escape Character: To match a string that contains a wildcard (like % or _), you need to instruct the LIKE operator to treat the % in 10% as a regular character. To do that, you need to explicitly specify an escape character after the ESCAPE clause:
expression LIKE pattern ESCAPE escape_character
-- example:
value LIKE '%10!%%' ESCAPE '!'
-- In this example, the ! is the escape character, it instruct the LIKE operator to treat the % in the 10% as regular character.

-- The following example finds all employees with the first name whose second character is h
SELECT employee_id, first_name, last_name
FROM employees WHERE first_name LIKE '_h%'
ORDER BY first_name;

-- The following example uses NOT LIKE to find all employees whose first name starts with S but not Sh
SELECT employee_id, first_name, last_name
FROM employees WHERE first_name LIKE 'S%' AND first_name NOT LIKE 'Sh%'
ORDER BY first_name;

-- ALL operator compares a value to all values in another value set. The All operator must be preceded by a comparison operator and followed by a subquery.
SELECT employee_id, first_name, last_name, salary
FROM employees WHERE salary >= ALL(SELECT salary FROM employees WHERE employee_id = 8)
ORDER BY salary DESC;

-- ANY operator compares a value to any value in a set according to the condition as shown below:
-- comparison_operator ANY(subquery). Similar to ALL operator, ANY operator must be precded by the comparison operator followed by a subquery
-- find all employees whose salaries are greater than the average salary of every department
SELECT employee_id, first_name, last_name, salary
FROM employees WHERE salary > ANY(SELECT AVG(salary) FROM employees GROUP BY department_id)
ORDER BY first_name, last_name;
-- Note that SOME is an alias for ANY, so you can use them interchangeably.

-- EXISTS operator tests is a subquery contains any rows:
-- EXISTS(subquery)
-- find all employees who have dependents
SELECT first_name, last_name
FROM employees WHERE EXISTS(SELECT 1 FROM dependents d WHERE employee_id = employee_id);

-- If a query uses so many OR operator, it will be difficult to read, you can use the IN instead
SELECT employee_id, first_name, last_name, hire_date
FROM employees WHERE YEAR(hire_date) = 2000 OR YEAR(hire_date) = 1999 OR YEAR(hire_date) = 1990
ORDER BY hire_date;

-- you can replace the OR with IN
SELECT employee_id, first_name, last_name, hire_date
FROM employees WHERE YEAR(hire_date) IN (1990, 1999, 2000)
ORDER BY hire_date;

-- NOT BETWEEN - to negate the value of BETWEEN, you use NOT BETWEEN
SELECT employee_id, first_name, last_name, salary
FROM employees WHERE salary NOT BETWEEN 2500 AND 2900
ORDER BY salary DESC;

-- YEAR() is used to extract the year from a date. If your database system doesn't support the YEAR() function use a similar function.
PostgreSQL - DATE_PART('year', hire_date)
Oracle - EXTRACT(year from hire_date)
MySQL, SQL server - YEAR(hire_date)

-- NOT In operator returns true if the expression does not equal any value in the list, otherwise false. To substitute the In operator, you can use != and AND operators as follows:
expression != value1 AND expression != value2 AND ...
-- Notice that if any value is NULL the IN operator returns no rows.

-- Subquery is a query that is nested in another query.

-- NOT greater than:
...
WHERE NOT salary > 5000