# SQL - Introduction

## Table of Contents

1. [What’s a Database](#whats-a-database)
2. [What’s a Relational Database](#whats-a-relational-database)
3. [What Does SQL Stand For](#what-does-sql-stand-for)
4. [What’s MySQL](#whats-mysql)
5. [How to Create a Database in MySQL](#how-to-create-a-database-in-mysql)
6. [What Does DDL and DML Stand For](#what-does-ddl-and-dml-stand-for)
7. [How to CREATE or ALTER a Table](#how-to-create-or-alter-a-table)
8. [How to SELECT Data from a Table](#how-to-select-data-from-a-table)
9. [How to INSERT, UPDATE, or DELETE Data](#how-to-insert-update-or-delete-data)
10. [What Are Subqueries](#what-are-subqueries)
11. [How to Use MySQL Functions](#how-to-use-mysql-functions)

## What’s a Database

A database is a structured collection of data that is organized and stored for easy retrieval and management. It serves as a digital repository where data can be stored, managed, and queried. Databases can range from simple collections of information to complex systems supporting applications with extensive data requirements.

## What’s a Relational Database

A relational database is a type of database that uses a tabular structure to store and organize data. It consists of tables, where each table represents a specific entity, and these tables are related to one another using keys. The relationships between tables make it possible to retrieve and manipulate data efficiently, while maintaining data integrity.

## What Does SQL Stand For

SQL stands for **Structured Query Language**. It is a domain-specific language used for managing and querying relational databases. SQL provides a standardized way to interact with databases, allowing users to define, manipulate, and retrieve data from them.

## What’s MySQL

MySQL is an open-source relational database management system (RDBMS) that is widely used for storing and managing structured data. It is known for its speed, reliability, and ease of use. MySQL supports SQL, making it a popular choice for web applications, data-driven websites, and many other types of software.

## How to Create a Database in MySQL

To create a database in MySQL, you can use the following SQL command:

```sql
CREATE DATABASE database_name;
```

Replace `database_name` with the desired name for your database. This command will create a new database with the specified name.

## What Does DDL and DML Stand For

- **DDL**: Data Definition Language. DDL is a subset of SQL used to define and manage the structure of database objects. It includes commands like `CREATE`, `ALTER`, `DROP`, and `TRUNCATE` for tables, schemas, and other database elements.

- **DML**: Data Manipulation Language. DML is a subset of SQL used to manage and manipulate data stored within the database. Common DML commands include `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.

## How to CREATE or ALTER a Table

To create a new table in MySQL, you can use the `CREATE TABLE` statement. Here's an example:

```sql
CREATE TABLE table_name (
  column1 datatype,
  column2 datatype,
  ...
);
```

To alter an existing table, you can use the `ALTER TABLE` statement. It allows you to add, modify, or delete columns in an existing table.

```sql
ALTER TABLE table_name
ADD column_name datatype;
```

## How to SELECT Data from a Table

To retrieve data from a table in MySQL, you can use the `SELECT` statement. Here's a basic example:

```sql
SELECT column1, column2
FROM table_name
WHERE condition;
```

This statement retrieves data from the specified columns in the table based on the provided condition.

## How to INSERT, UPDATE, or DELETE Data

- **INSERT**: To add new records to a table, you can use the `INSERT INTO` statement.

```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

- **UPDATE**: To modify existing data in a table, use the `UPDATE` statement.

```sql
UPDATE table_name
SET column1 = new_value1, column2 = new_value2
WHERE condition;
```

- **DELETE**: To remove records from a table, use the `DELETE FROM` statement.

```sql
DELETE FROM table_name
WHERE condition;
```

## What Are Subqueries

A subquery is a query embedded within another query. It allows you to retrieve data from one table based on the results of another query. Subqueries can be used in various parts of a SQL statement, such as the `SELECT`, `FROM`, or `WHERE` clauses, and they are powerful tools for complex data retrieval.

## How to Use MySQL Functions

MySQL provides a wide range of built-in functions that can be used to perform operations on data. These functions can be used in SQL statements to transform or manipulate data. For example, you can use functions like `COUNT`, `SUM`, `AVG`, `CONCAT`, and many others to perform calculations or format data in your queries.

```sql
SELECT AVG(salary) FROM employees;
```

In this example, the `AVG` function is used to calculate the average salary of employees in a table.

For more information on SQL, MySQL, and specific SQL functions, consult the official documentation and other relevant resources.

This README provides an introduction to SQL and MySQL, covering fundamental concepts and essential SQL commands. For more in-depth information and practical examples, please refer to additional learning resources and documentation.