/*
Grouping is one of the most important tasks that you have to deal with while working with data. To group rows, you use GROUP BY clause.

The GROUP BY clause is an optional clause of the SELECT statement that combines rows into groups based on matching values in specified columns. One row is returned for each group.
You often use the GROUP By in conjunction with an aggregate function such as MIN, MAX, AVG, SUM, or COUNT to calculate a measure that provides the information for each group.
Syntax:

SELECT column1, column2,
AGGREGATE_FUNCTION(column3)
FROM table1 
GROUP BY column1, column2;

It is not mandatory to include an aggregate function in the SELECT clause. However, if you use an aggregate function, it will calculate the summary value for each group.
If you want to filter the rows before grouping, you add a WHERE clause. However, to filter groups, you use the HAVING clause.
It is important to emphasize that the WHERE clause is applied before rows are grouped whereas the HAVING clause is applied after rows are grouped. In other words, the WHERE clause is applied to rows whereas the HAVING clause is applied to groups. To sort the groups, you add the ORDER BY clause after the GROUP BY clause. The columns that appear in the GROUP BY clause are called grouping columns. If a grouping column contains NULL values, all NULL values are summarized into a single group because the GROUP BY clause considers NULL values are equal.
*/
-- to find the headcount of each department, you group the employees by department_id column, and apply the COUNT function to each group as the following query:
SELECT department_id, COUNT(employee_id) headcount
FROM employees GROUP BY department_id;

/*
GROUP BY with INNER JOIN
To get the department name, you join the employees table with the departments table as follows:
*/
SELECT e.department_id, department_name, COUNT(employee_id) headcount
FROM employees e 
INNER JOIN departments d ON d.department_id = e.department_id
GROUP BY e.department_id;

-- GROUP BY with ORDER BY
SELECT e.department_id, department_name, COUNT(employee_id) headcount
FROM employees e 
INNER JOIN departments d ON d.department_id = e.department_id
GROUP BY e.department_id 
ORDER BY headcount;
-- you can use either the headcount alias or you can use COUNT(employee_id) in the ORDER BY clause

-- GROUP BY with HAVING
-- To find the department whose headcount is greater than 5, you use the HAVING clause like the following query:
SELECT e.department_id, department_name, COUNT(employee_id) headcount
FROM employees e 
INNER JOIN departments d ON d.department_id = e.department_id
GROUP BY e.department_id 
HAVING headcount > 5
ORDER BY headcount DESC;

-- GROUP BY with MIN, MAX, and AVG
-- the following query returns the minimum, maximum, and average salary of employees in each department.
SELECT e.department_id, department_name, MIN(salary) min_salary, 
MAX(salary) max_salary, ROUND(AVG(salary), 2) average_salary
FROM employees e 
INNER JOIN departments d ON d.department_id = e.department_id
GROUP BY e.department_id;

-- GROUP BY with SUM function
-- to get the total salary per department you apply the SUM function to the salary column and group employees by the department_id column as follows:
SELECT e.department_id, department_name, SUM(salary) total_salary
FROM employees e 
INNER JOIN departments d ON d.department_id = e.department_id
GROUP BY e.department_id;

-- GROUP BY multiple columns
-- The following groups rows with the same values in both department_id and job_id columns in the same group then return the rows for each of the groups
SELECT e.department_id, department_name, e.job_id, job_title, COUNT(employee_id)
FROM employees e 
INNER JOIN departments d ON d.department_id = e.department_id
INNER JOIN jobs j ON j.job_id = e.job_id
GROUP BY e.department_id, e.job_id;

-- GROUP BY and DISTINCT
-- if you use the GROUP BY without an aggregate clause, the GROUP BY behaves like the DISTINCt operator.
SELECT phone_number FROM employees GROUP BY phone_number;

/*
SQL HAVING clause
SELECT column1, column2,
AGGREGATE_FUNCTION (column3)
FROM table1
GROUP BY column1, column2
HAVING group_conditon;

Note that the HAVING clause appears immediately aftr the GROUP BY clause

HAVING vs, WHERE,

“The WHERE clause applies the condition to individual rows before the rows are summarize into groups
by the GROUP BY clause. However the HAVING clause applies the condition to the groups after the
ows are grouped imo groups.

“Therefore it is important to note that the HAVING clause is applied after whereas the WHERE clause is
applied before the GROUP BY clause,

SQL HAVING clause examples
To gt the managers and their direct reports, you use the GROUP BY clause to group employees by the
managers and use the COUNT function to count the direct reports.

The following query illustrates the ides

SELECT manager_id, first_name, last_name, COUNT employee_id) direct_reports
FROM employees WHERE manager_id IS NOT NULL
GROUP BY manager_id;

To find the managers who have atleast five direct reports, you add a HAVING clause to the query above
as the following

SELECT manager id, fist_name, last name, COUNT(employee_ id) direct_reports
FROM employees WHERE manager_id IS NOT NULL
GROUP BY manager_id
HAVING direct_reports >= 5;

SQL HAVING with SUM function example

The following statement calculates the sum of salary that the company pays for each department and
selects ony the departments with the sum of salary between 20000 and 30000,

SELECT department_id, SUM(salary)
FROM employees GROUP BY department_id
HAVING SUM(salary) BETWEEN 20000 AND 30000
ORDER BY SUM(salary);


SQL HAVING with MIN funetion example
To find the department that has employees wth the lowest salary greater than 10000, you use the
following query

SELECT e.department_id, department_name, MIN(salary)
FROM employees e
INNER JOIN departments d ON d.department_id = e.department_id
GROUP BY e.department_id
HAVING MIN(salary) >= 10000
ORDER BY MIN(salary);

How the query works.
1. First use the GROUP BY clause to groups employees by department.
2. Second, use the MIN function to find the lowest salary per group.
3. Third, apply the condition to the HAVING clause

SQL HAVING clase with AVG function example
To find the departments that have the average salaries of employees between 5000 and 7000, you use
the AVG function as the following query

SELECT e.department_id, department_name, ROUND(AVG(salary),2)
FROM employees e
INNER JOIN departments d ON d.department_id = e.department_id 
GROUP BY e.department_id
HAVING AVG(salary) BETWEEN 5000 AND 7000
ORDER BY AVG(salary);
*/