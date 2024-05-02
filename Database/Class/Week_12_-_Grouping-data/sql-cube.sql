/*
SOL CUBE
Introduction to SQL CUBE,
Similar to the ROLLUP, CUBE is an extension of the GROUP BY clause. CUBE allows you to generate
subtotal like the ROLLUP extension. In adition, the CUBE extension will generate subtotals for all
combinations of grouping columns specified in the GROUP BY clause

The following illustrates the syntax of CUBE extension:

SELECT c1, c2, aggregate_function(c3)
FROM table_name
GROUP BY CUBE(c1, c2);

In this syntax, we have two columns specified in the CUBE. The statement creates two subtotal
combinations. Generally if you have a number of columns listed in the CUBE, the statement will create
2n subtotal combinations

SQL CUBE examples
We will reuse the inventory table created in the ROLLUP tutorial.

SQL CUBE with ne column example
The following statement uses the SUM() function and the GROUP BY clause to find the total inventory
of every warehouse:

SELECT warehouse, SUM(quantity)
FROM inventory
GROUP BY warehouse;

If you want to know the total inventory in all warehouses, you use the CUBE extension in the GROUP BY clause as follows:

SELECT warehouse, SUM(quantity)
FROM inventory
GROUP BY CUBE(warehouse)
ORDER BY warehouse;

In this example, the CUBE extension add total inventory row with a null value in the warchouse column. The effect is the same as the ROLLLUP function. To make the output more readable, you can use the COALESCE() function as shown below:

SELECT
  COALESCE(warehouse, 'All warehouses'), SUM(quantity)
FROM inventory
GROUP BY CUBE (warehouse)
ORDER BY warehouse;

SQL CUBE with multiple columns example
The following statement finds the total inventory by warehouse and product:

SELECT warehouse, product, SUM(quantity)
FROM inventory
GROUP BY warehouse, product
ORDER BY warehouse, product;

When you use the CUBE function, the query makes four subtotals:
SELECT warehouse, product, SUM(quantity)
FROM inventory
GROUP BY CUBE(warehouse, product)
ORDER BY warehouse, product;

As you can see in the output, we have four subtotal rows

1. The third and sixth rows show the total inventory of all products in the San Francisco and San Jose warehouses. The values in the product column are null

2. The seventh and eighth rows display the total inventory by products which are Samsung and iPhone in all warehouses. Hence, the values in the warehouse columns are null.

The last column is the grand total that shows the total inventory in all warehouses

The following statement uses the COALESCE() function to substitute null values by more meaningful data:

SELECT
COALESCE(warehouse, '...All Warehouses') warehouse,
COALESCE(product, '...All Products') product,
SUM(quantiy)
FROM inventory
GROUP BY CUBE (warehouse, product)
ORDER BY warehouse, product;


Creating cross-tabular reports
The following query creates a cross-tabular report by retrieving data from the employees table in the sample database using the CUBE extension:

SELECT
COALESCE(department_name, '-') department,
COALESCE(job_tite, '-') job,
COUNT(*),
SUM(salary) salary
FROM employees
INNER JOIN departments USING(department_id)
INNER JOIN jobs USING(job_id)
GROUP BY CUBE(department_name, job_tite)
ORDER BY department_name ASC NULLS LAST;
*/