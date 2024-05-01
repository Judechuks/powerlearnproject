/*
Name: Monye Jude Chukwuemeke
PLP – Database Module
Week 9 Task
Question:
Create a database with a table named Books with columns BookID, Title, Author, Genre, and PublicationYear. Populate the table with sample data. Write SQL queries to perform the following tasks:
Retrieve all columns for books published in the year 2020.
Find the distinct genres available in the Books table.
Alias the column Author as BookAuthor in a query result.
*/

CREATE DATABASE book_record;

USE book_record;

-- creating table
CREATE TABLE Books(
  BookID INT PRIMARY KEY,
  Title VARCHAR(255), 
  Author VARCHAR(255), 
  Genre  VARCHAR(50), 
  PublicationYear INT
);

-- populating table
INSERT INTO Books (BookID, Title, Author, Genre, PublicationYear)
VALUES
(1, "Introduction to SQL", "Harper James", "Programming", 2005),
(2, "Introduction to Software Engineering", "Scot MacMillian", "software development", 2020),
(3, "Pride and Prejudice", "Jane Austen", "Romance", 1813),
(4, "Introduction to HTML", "Barner Tee", "Computer science", 1920),
(5, "Programming in Python", "Davison Philips", "Programming", 2020),
(6, "Brave New World", "Aldous Huxley", "Science Fiction", 1932);

-- Retrieving all columns of books published in the year 2020
SELECT * FROM Books WHERE PublicationYear = 2020;

-- Finding distinct genres available in the Books table.
SELECT DISTINCT Genre FROM books;

-- Aliasing the column Author as BookAuthor.
SELECT BookID, 
Title,
Author AS BookAuthor, 
Genre, 
PublicationYear 
FROM Books;