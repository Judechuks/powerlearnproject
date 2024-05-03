/*
Name: Monye Jude Chukwuemeke
PLP - Software Development
Database Module
Week 12 Task
Question:
Create a database with a table named Sales with columns ProductID, Category, QuantitySold, and Revenue. Populate the table with sample data. Write SQL queries to perform the following tasks:

1. Calculate the total quantity sold and revenue for each product category.
2. Find the average revenue per unit sold for each product category.
3. Identify the product categories with the highest total revenue.
*/

-- creating a SalesDB database
CREATE DATABASE SalesDB;

-- using the SalesDB database
USE SalesDB;

-- creating Sales table
CREATE TABLE Sales(
  productID INT PRIMARY KEY,
  Category VARCHAR(255),
  QuantitySold INT,
  Revenue NUMERIC
);

-- populating the Sales table with data
INSERT INTO Sales (ProductID, Category, QuantitySold, Revenue)
VALUES
    (1, 'Electronics', 100, 5000.00),
    (2, 'Electronics', 150, 7000.00),
    (3, 'Clothing', 200, 8000.00),
    (4, 'Clothing', 180, 7500.00),
    (5, 'Furniture', 130, 7000.00),
    (6, 'Electronics', 50, 2500.00),
    (7, 'Clothing', 70, 3000.00),
    (8, 'Furniture', 80, 4000.00),
    (9, 'Electronics', 80, 3500.00),
    (10, 'Clothing', 100, 4500.00);

-- task 1: Calculating the total quantity sold and revenue for each product category
SELECT Category, SUM(QuantitySold) TotalQuantitySold, SUM(Revenue) TotalRevenue
FROM Sales
GROUP BY Category;

-- task 2: Finding the average revenue per unit sold for each product category.
SELECT Category, AVG(Revenue / QuantitySold) AvgRevenuePerUnitSold
FROM Sales
GROUP BY Category;

-- task 3: Identifying the product categories with the highest total revenue.
SELECT Category, SUM(Revenue) TotalRevenue
FROM Sales
GROUP BY Category
ORDER BY TotalRevenue DESC
LIMIT 1;