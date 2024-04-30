/*
The SQL ORDER BY clause is used to sort the result set of a query in ascending (default) or descending order based on one or more columns. It is often used with the SELECT statement to organize the output of a query.

SELECT column1, column2, ...
FROM table_name
ORDER BY column1 [ASC | DESC], column2 [ASC | DESC], ...;  
*/

-- Retriieve and sort students names alphabetically
SELECT First_Name, Last_Name
FROM studentsdb.students
ORDER BY First_Name ASC; 

-- Retriieve and sort students names sorting StudentsID in descending order
SELECT First_Name, Last_Name
FROM studentsdb.students
ORDER BY StudentID DESC;  

/*
SELECT employee_name, department, salary
FROM employees
ORDER BY department ASC, salary DESC;  

*/
