-- CREATE DATABASE candyShop; 

-- USE candyShop;

/*
CREATE TABLE Items(
ItemID INT PRIMARY KEY,
ItemName VARCHAR(200),
ItemPrice VARCHAR(100),
ExpiryDate DATE
);
*/

/*
INSERT INTO Items(ItemID, ItemName, ItemPrice, ExpiryDate)
VALUES
('100', 'Ice cream', '20', '2024-07-02'),
('101', 'Snacks', '30', '2025-05-01'),
('102', 'Chocolate', '25', '2025-06-01'),
('103', 'Sweets', '10', '2025-07-03'),
('104', 'Doughnuts', '35', '2025-10-11'),
('105', 'Milky Doughnut', '30', '2025-05-10'),
('106', 'Digestive Biscuit', '50', '2025-08-11'),
('107', 'Chocolate Candy', '15', '2024-09-12'),
('108', 'Strawberry Lollipop', '10', '2025-06-19'),
('109', 'Burger', '40', '2024-08-22'),
('110', 'Bubblegum', '15', '2025-04-28');
*/

-- SELECT * FROM Items
-- slect all the columns and data from the Items table

/*
SELECT ItemID, ItemName FROM Items 
WHERE ItemID = 102;
-- selects 2 columns from Items table
*/

/*
SELECT ItemID, ItemName FROM Items 
WHERE ItemName = 'Bubblegum';
-- selects 2 columns from Items table
*/

-- DROP TABLE tableName; 
-- to delete a table

-- to update a column's name (attribute's name)
/*
UPDATE Items
SET ItemPrice = 'Item_Price';
*/

-- to delete a column
/*
ALTER TABLE Items
DROP COLUMN ExpiryDate;
*/