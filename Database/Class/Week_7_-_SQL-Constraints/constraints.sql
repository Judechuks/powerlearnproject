/*
Constraints are rules that are enforced on the data column of a table that limits the type of data that goes into the table which helps to enforce data integrity and consistency. This ensures accuracy and reliability of data in the database.
Constraint could either be column level or table level. The column level constraints are applied only to one column, whereas the table level constraints are applied to the whole table.
Some of these constraints includes:

1. NOT NULL
In SQL, the NOT NULL constraint is a crucial feature used to ensure data integrity by specifying that a column must contain a value, and it cannot be left empty or filled with a null value. This constraint is typically used when you want to enforce the presence of data in a specific column, preventing the insertion of records with missing or undefined values. 

ALTER TABLE with NOT NULL Statement
To add or remove the NOT NULL constraint from an existing table, you can use the ALTER TABLE statement. This statement allows you to make structural changes to an existing table, including modifying the constraints applied to its columns. Here's how you can use the ALTER TABLE statement to set a column as NOT NULL or to remove the constraint:
*/
ALTER TABLE tableName
MODIFY columnName datatype NOT NULL;

-- Removing the NOT NULL Constraint:
ALTER TABLE tableName
MODIFY columnName datatype;

/*
2. PRIMARY KEY
In SQL, a primary key is a fundamental concept used to define a unique identifier for each record in a database table. It enforces data integrity and ensures that each row in the table has a distinct value in the primary key column. The primary key constraint is a database constraint that ensures the uniqueness and non-nullity of values in a designated column or set of columns.
*/
CREATE TABLE tableName(
  column1 datatype PRIMARY KEY,
  column2 datatype,
);

-- Adding a primary key with the ALTER TABLE STATEMENT
ALTER TABLE tableName
ADD PRIMARY KEY (column1);

-- Removing a primary key constraint
ALTER TABLE tableName
DROP PRIMARY KEY;

/*
3. FOREIGN KEY
In SQL, a foreign key constraint is a database feature used to establish a relationship between two tables by enforcing referential integrity. This constraint ensures that the values in a specific column or set of columns in one table correspond to values in another table's primary key. By doing so, it maintains the consistency and accuracy of data within a database. A foreign key constraint is primarily used to create relationships between tables, typically to reflect associations between data entities. Here's how it works with an example:
Suppose you have two tables: "Orders" and "Customers." In the "Orders" table, you want to associate each order with a customer by using the "CustomerID" column. The "CustomerID" column in the "Orders" table will reference the "CustomerID" column in the "Customers" table, which is the primary key of the "Customers" table.
*/
-- Creating a foreign key constraint
CREATE TABLE Orders(
OrderID INT PRIMARY KEY,
OrderNumber INT NOT NULL,
CustomerID INT FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID));

-- OR

CREATE TABLE Orders(
OrderID INT PRIMARY KEY,
OrderNumber INT NOT NULL,
CustomerID INT,
FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID));

-- OR 

CREATE TABLE Orders(
OrderID INT,
OrderNumber INT NOT NULL,
CustomerID INT,
PRIMARY KEY (OrderID),
CONSTRAINT FK_CustomerID FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID));

-- Adding a FOREIGN KEY Constraint to Existing Table
ALTER TABLE tableName
ADD CONSTRAINT constraintName -- usually FK_ColumnName
FOREIGN KEY (column1)
REFERENCES referencedTable(referencedColumn);

-- Removing a Foreign Key Constraint 
ALTER TABLE tableName
DROP CONSTRAINT constraintName
/*
QUESTION:
CREATE TABLE Orders(
OrderID INT,
OrderNumber INT NOT NULL,
CustomerID INT,
PRIMARY KEY (OrderID)
CONSTRAINT FK_CustomerID FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID));
-- from this code can i drop the foreign key using
-- ALTER TABLE Orders DROP FOREIGN KEY FK_CustomerID since the constraint wasn't named?
ANSWER:
Certainly! Let’s address your question about dropping the foreign key constraint.
In your provided CREATE TABLE statement, you’ve defined a foreign key constraint without explicitly naming it. The constraint is associated with the CustomerID column in the “Orders” table, referencing the CustomerID column in the “Customers” table.
To drop this unnamed foreign key constraint, you can use the appropriate syntax based on your database system:
MySQL:
To remove the foreign key constraint, use the following SQL:
ALTER TABLE Orders DROP FOREIGN KEY FK_CustomerID;
Even though the constraint wasn’t explicitly named, you can still reference it by the default system-generated name (which includes the table name and column name).
*/

/*
4. UNIQUE 
In SQL, a unique constraint is a database feature that ensures that the values in a specific column or set of columns are unique among all the rows in a table. It guarantees that no duplicate values are allowed in the designated column(s), which is vital for maintaining data integrity.

Unique vs. Primary Key Constraint
While both unique and primary key constraints serve to enforce data integrity and uniqueness, they have distinct characteristics:

Unique Constraint:
Allows one unique value in the column(s).
Allows NULL values, meaning a unique constraint can have multiple NULL values.
Can be applied to multiple columns.
Often used when you want to ensure the uniqueness of data, but not necessarily as an identifier for records.

Primary Key Constraint:
Implies a unique constraint, but with the added condition that the column(s) cannot contain NULL values.
Serves as a unique identifier for each record in a table.
Usually applied to a single column (though composite primary keys, using multiple columns, are also possible).
*/

-- Creating a unique constraint while creating a table
CREATE TABLE tableName (
column1 datatype UNIQUE, 
column1 datatype 
);

-- Adding a unique constraint on existing table
ALTER TABLE tableName 
ADD CONSTRAINT constraintName UNIQUE (column1);
-- example
ALTER TABLE Emails 
ADD CONSTRAINT UC_EmailAddress UNIQUE (EmailAddress);

-- Removing a unique constraint
ALTER TABLE tableName 
DROP CONSTRAINT constraintName;

/*
5. CHECK
Check constraint validates data before it is stored in one or more columns based on a boolean expression.
Syntax: 
CHECK (boolean_expression) OR
CONSTRAINT constraint_name CHECK (boolean_expression)

The check constraint is satisfied is the boolean expression returns TRUE or NULL, It returns NULL when any of the operands is NULL, they will not prevent NULL value in the constrained column. To make sure that the column does not contain a NULL value, use the NOT NULL constraint. Example:
*/
CREATE TABLE products(
product_ID INT PRIMARY KEY,
product_name VARCHAR(255) NOT NULL,
selling_price NUMERIC (10,2) CHECK (selling_price > 0)
-- implicit contraint_name is columnName_chk_n, where n can be 1, 2, 3 ..., for first, second, third etc
);

-- creating a check constraint with a constraint name
CREATE TABLE products(
product_ID INT PRIMARY KEY,
product_name VARCHAR(255) NOT NULL,
selling_price NUMERIC (10,2) CONSTRAINT positive_selling_price CHECK (selling_price > 0)
);

-- you can define a check constraint that refers to multiple columns
CREATE TABLE products(
product_ID INT PRIMARY KEY,
product_name VARCHAR(255) NOT NULL,
selling_price NUMERIC (10,2) CHECK (selling_price > 0), -- column constraint
cost_price NUMERIC (10,2) CHECK (cost_price > 0), -- column constraint
CHECK (selling_price > cost_price) -- table constraint
);

-- assigning the table constraint a name
CREATE TABLE products(
product_ID INT PRIMARY KEY,
product_name VARCHAR(255) NOT NULL,
selling_price NUMERIC (10,2) CHECK (selling_price > 0), -- column constraint
cost_price NUMERIC (10,2) CHECK (cost_price > 0), -- column constraint
CONSTRAINT valid_selling_price CHECK (selling_price > cost_price) -- table constraint
);
