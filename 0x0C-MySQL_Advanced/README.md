# 0x0C-MySQL_Advanced

MySQL database project

## Resources:

- <a href="https://devhints.io/mysql" target="_blank_blank">MySQL cheatsheet</a>
- <a href="https://www.liquidweb.com/kb/mysql-optimization-how-to-leverage-mysql-database-indexing/" target="_blank">MySQL Performance: How To Leverage MySQL Database Indexing</a>
- <a href="https://www.w3resource.com/mysql/mysql-procedure.php" target="_blank">Stored Procedure</a>
- <a href="https://www.w3resource.com/mysql/mysql-triggers.php" target="_blank">Triggers</a>
- <a href="https://www.w3resource.com/mysql/mysql-views.php" target="_blank">Views</a>
- <a href="https://dev.mysql.com/doc/refman/5.7/en/functions.html" target="_blank">Functions and Operators</a>
- <a href="https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html" target="_blank">Trigger Syntax and Examples</a>
- <a href="https://dev.mysql.com/doc/refman/5.7/en/create-table.html" target="_blank">CREATE TABLE Statement</a>
- <a href="https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html" target="_blank">CREATE PROCEDURE and CREATE FUNCTION Statements</a>
- <a href="https://dev.mysql.com/doc/refman/5.7/en/create-index.html" target="_blank">CREATE INDEX Statement</a>
- <a href="https://dev.mysql.com/doc/refman/5.7/en/create-view.html" target="_blank">CREATE VIEW Statement</a>

## Learning Objectives:

In this projects we learn about:

- How to create tables with constraints
- How to optimize queries by adding indexes
- What is and how to implement stored procedures and functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL

## Extras:

- useful operators for matching in mysql:
    - we note that using these operators lowers the performance of indexing in db
    - `LIKE` operator used with WHERE
```
SELECT * FROM db WHERE style LIKE "%Glam rock%"
```
    - `REGEXP` operator same as like but for matching using regex
```
SELECT * FROM db WHERE style REGEXP '.*Glam rock.*'
```

## Author
- Yassine Chayrrou
