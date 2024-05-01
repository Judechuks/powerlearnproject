/*
💡The limit clause is widely supported by manay database systems. However, the LIMIT cklause is not in SQL standard. SQL:2008 introduced OFFSET FETCH clause which have similar function to the LIMIT clause. The OFFSET FETCH clause allows you to skip N first rows in a result set before starting to return any rows.
The following shows the syntax of SQL FETCH clause:

OFFSET offset_rows {ROWROWS}
FETCH {FIRSTNEXT} [fetch_rows] {ROWROWS} ONLY

In this syntax:
💡The ROW and ROWS, The FIRST and NEXT are the synonymns. Therefore, you can use them interchangeably. 
💡The offset_rows is an integer number which number be zero or positive. In case the offset_rows is greater than the number of rows in the result set, no rows will be returned.
💡The fetch_rows is also an integer numberthat determines the number of rows to be returned. The value of fetch_rows is equal to or greater than one.

Because rows are stored in the table in an unspecified order, you should always use the FETCH clause with the ORDER BY clause to get consistent output.
The OFFSET FETCH  clause it typically used in the client or web appications that require pagination. For example. if each page has ten rows, to get the rows of the second page, you can skip the first ten rows and return the next ten rows.

SQL FETCH examples:
The following statement returns the first employee who have the highest salary:
*/
SELECT employee_id, first_name, last_name, salary
FROM employees ORDER BY salary DESC
OFFSET 0 ROWS FETCH NEXT 1 ROWS ONLY;
-- in this example, the OREDR BY clause sorts the employees by salary from high to low, The OFFSET clause skips zero rows and the FETCH clause returns the first row.

-- The following statement sorts the employees by salary, skips the first 5 employees with the highest salary, and fetches the next fives ones.
SELECT employee_id, first_name, last_name, salary
FROM employees ORDER BY salary DESC
OFFSET 5 ROWS FETCH NEXT 5 ROWS ONLY;

/*
summary:
💡 Use the SQL FETCH clause to limit the number of rows returned by a query.
💡 The SQL FETCH clause skips N rows in a result set before starting to return any rows.
*/