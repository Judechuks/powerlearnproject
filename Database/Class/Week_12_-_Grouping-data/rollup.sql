/*
SQL ROLLUP
Introduction to SQL ROLLUP
The ROLLUP is an extension of the GROUP BY clause, The ROLLUP option allows you to include
extra rows that represent the subtotals, which are commonly referred to as super-aggregate rows, along
with the grand total row. By using the ROLLUP option. you can use a single query to generate multiple grouping sets.
Note that grouping set is a set of columns by which you group. For example, a query that returns the
inventory by the warehouse, the grouping set is (warehouse).

SELECT warehouse, SUM(quantity) qty
FROM inventory
GROUP BY warehouse;

For more information about the GROUPING SETS, check it out the grouping set tutorial

The following illustrates the basic syntax of the SQL ROLLUP:

SELECT c1, c2, aggregate_function(c3)
FROM table GROUP BY ROLLUP (c1, c2);

The ROLLUP assumes a hierarchy among the input columns. For example, ithe inpat column is (c1, c2),
the hierarchy c1 > c2. The ROLLUP generates all grouping sets that make sense considering this hierarchy. This is why we often use ROLLUP to generate the subtotals and the grand total fo reporting purposes.

In the syntax above, ROLLUP(c1, c2) generates three following grouping sets

(c1, c2), (c1), ()

This syntax is supported by Oracle, Microsoft SQL Server, and PostgreSQL. However, MySQL has a slightly different syntax as shown below:

SELECT c1, c2, aggregate_function(c3)
FROM table_name GROUP BY c1, c2 WITH ROLLUP;

SQL ROLLUP examples
We will use the inventory table that we set up in the GROUPING SETS tutorial for the demonstration.

SQL ROLLUP with one column example
The following statement uses the GROUP BY clause and the SUM() functon to find the total inventory by warehouse:

SELECT warehouse, SUM(quantity)
FROM inventory
GROUP BY warehouse;

To retrieve the total products in all warehouses, you add the ROLLUP to the GROUP BY clause as follows:

SELECT warehouse, SUM(quantity)
FROM inventory
GROUP BY ROLLUP(warehouse);

As you can see in the result, the NULL value in the warehouse column specifies the grand total super-aggregate line. In this example, the ROLLUP option causes the query to produce another row that shows the total poducts in all warehouses.

To make the output more readable, you can use the COALESCE() function to substitute the NULL value by the All warehouses as follows:

SELECT
  COALESCE(warehouse, 'All warehouses') AS warehouse, SUM(quantity)
FROM inventory
GROUP BY ROLLUP(warehouse);

SQL ROLLUP with multiple columns example
The following statement calculates the inventory by warehouse and product:

SELECT warehouse, product, SUM(quantity)
FROM inventory
GROUP BY warehouse, product;

Let's add the ROLLUP to the GROUP BY clause:

SELECT warehouse, product, SUM(quantity)
FROM inventory
GROUP BY ROLLUP(warehouse, product);

Note that the output consists of summary information at two levels of analysis, not just one:

1. Following each set of product rows for a specified warehouse, an extra summary row appears
displaying the total inventory. In these rows, values in the product column set to NULL.
2. Following all rows, an extra summary row appears showing the total inventory of all warehouses and products. In these rows, the values in the warehouse and product columns set to NULL.

SQL ROLLUP with partial rollup example
You can use ROLLUP to perform partial roll-up that reduces the number of subtotals calculated as shovwn in the following example:

SELECT warehouse, product, SUM(quantity)
FROM inventory
GROUP BY warehouse, ROLLUP(product);

In this example, the ROLLUP only makes super-aggregate summary for the product column, not the warehouse column.
*/