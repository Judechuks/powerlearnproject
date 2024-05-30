/*
SQL Aliases
Column Alias syntax:
column_name AS alias_name;

if the alias contains space, you can put it into a single or double quote.
column_name AS 'alias name';
*/
SELECT in_no AS 'Invoice Number', amount, due_date AS 'Due Date', cust_no 'Customers Number'
FROM invoices;
-- notice the cust_no has no AS keyword, you can exclude it