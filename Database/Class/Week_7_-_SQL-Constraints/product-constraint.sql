USE candyshop;

-- creating a check constraint, to ensure selling price is not a negative value
CREATE TABLE products(
product_ID INT PRIMARY KEY,
product_name VARCHAR(255) NOT NULL,
selling_price NUMERIC (10,2) CHECK (selling_price > 0)
);