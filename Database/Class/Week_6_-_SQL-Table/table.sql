-- Creating a database
CREATE DATABASE databaseName;

-- making use of the database
USE databaseName;

-- Creating a table
CREATE TABLE tableName(column1 datatype, column2 datatype, column3 datatype);

-- Inserting data into the table
INSERT INTO tableName(column1, column2, column3)
VALUES 
('column1 value', 'column2 value', 'column3 value'),
('column1 value', 'column2 value', 'column3 value'),
('column1 value', 'column2 value', 'column3 value');


/*
ALTER TABLE
The SQL ALTER TABLE statement is a powerful command that allows you to make structural changes to an existing database table. One common operation is adding a new column to a table.

1. Add a Column:
This can be necessary when you need to include additional information or adapt your database schema to changing requirements. Here's how you can use the SQL ALTER TABLE statement to add a column to an existing table:
*/
ALTER TABLE tableName
ADD columnName datatype;

/*
2. Modify a Column:
The ALTER TABLE statement can also be used to modify existing columns in a table. This is helpful when you need to change datatype, length, or other attributes of a column. Here's is how you can modify a column:
*/
ALTER TABLE tableName
MODIFY columnName new_datatype;

/*
3. Drop a Column:
Sometimes, you may need to remove a column from a table if it's no longer needed or if the schema changes. The ALTER TABLE statement can be used to drop or delete a column. Here's the syntax for dropping a column:
*/
ALTER TABLE tableName
DROP COLUMN columnName;

-- Dropping a table means deleting a table
-- Dropping a single table
DROP TABLE tableName;

-- Dropping multiple tables
DROP TABLE tableName1, tableName2, tableName3, ..., tableNameN;
