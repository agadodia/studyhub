## Database Notes  - (Compiled by Anju Gadodia)

</br>

## DATABASES
- **What Is a database?** A database is a collection of bits of data that is organized into files, which are called **tables**. Tables are a logical way of accessing, managing, and updating data.

- A **Relational Database** is a collection of data items with predefined relationships between them. They require a fixed definition of the structure of the data. A Relational database is also called as SQL DataBase
- A **Non-relational database** is a database that does not follow the relational model.NoSQL databases use various data models for accessing and managing data. These types of databases are optimized specifically for applications that require large data volumes, low latency, and flexible data models. These requirements are achieved by relaxing some of the restrictions around data consistency that are used by other databases.
</br>
</br>

 **How do you manage data?**</br> 
 You manage stored data with a database management system (DBMS). A database management system (DBMS) is software or database-as-a-service (DBaaS). It is used mainly for creating databases; inserting data into a database; and storing, retrieving, updating, or deleting data in the database.

 A **Data Lake** is a centralized repository that stores, manages, and distributes all kinds of data that an organization creates, stores, and operates. Types of data can include data from user database applications, files, or documents. You can store your data as-is, without needing to structure the data first.

 **With SQL, you use SQL statements to perform many of the necessary actions on a database. The sublanguages of SQL groups are as follows:**
-  Data manipulation language (DML) -for accessing, Inserting and deleteing rows in the tables ex SELECT,INSERT,UPDATE,DELETE 
-  Data definition language (DDL) -for defining of the database and tables ex CREATE, ALTER TABLE ,DROP
-  Data control language (DCL)-for Controlling the access to a database ie. Giving permissions to specifiec users to specific tables ex.REVOKE,GRANT

![Sql Sublanguages](/images/Databases/dbDefinition.png)

**SQL has three kinds of data types:**

* predefined
* constructed
* user-defined

**Numeric DataTypes**

|Numeric Types	|Description            |
| ------------- |:---------------------:|
|  TINYINT	    |A very small integer   |
|  MEDIUMINT	|A medium-sized integer   |  
|  INT	        |A standard integer   |
|  BIGINT		|A large integer   |
|  DECIMAL      |A fixed-point number   |
|  FLOAT	    |A single-precision floating point number  |
|  DOUBLE	    |A double-precision floating point number   |
|  BIT	    |A bit field   |

**MySQL Boolean data type**

-MySQL does not have the built-in BOOLEAN or BOOL data type. To represent boolean values, MySQL uses the smallest integer type which is TINYINT(1). In other words, BOOLEAN and BOOL are synonyms for TINYINT(1). 

**MySQL String data types**
|String Types	|Description            |
| ------------- |:---------------------:|
|  CHAR	    |A fixed-length nonbinary (character) string   |
|  VARCHAR	|A variable-length non-binary string  |  
|  BINARY	        |A fixed-length binary string  |
|  VARBINARY		|A variable-length binary string   |
|  TINYBLOB      |A very small BLOB (binary large object)  |
|  BLOB	    |A small BLOB number  |
|  MEDIUMBLOB	    |A medium-sized BLOB point number   |
|  LONGBLOB	    |A large BLOB  |
|  TINYTEXT	    |A small non-binary string  |
|  MEDIUMTEXT	    |A medium-sized non-binary string  |
|  LONGTEXT	    |A large non-binary string  |
|  ENUM	    |An enumeration; each column value may be assigned one enumeration member  |
| SET	|A set; each column value may be assigned zero or more SET members        |
 



**Information in a database is stored in tables. Each table has columns or names of fields under which data is stored in rows.**

**There are mainly Three types of joins-**
- Inner Join
- Outer join (Left-Outer,Right-Outer,Full-Outer)
- Self join

A **union** is a merging of two tables. 

Supported Types of Joins in MySQL

    INNER JOIN: Returns records that have matching values in both tables
    LEFT JOIN: Returns all records from the left table, and the matched records from the right table
    RIGHT JOIN: Returns all records from the right table, and the matched records from the left table
    CROSS JOIN: Returns all records from both tables

## Joins-

![This is inner join.](/images/Databases/img_innerjoin.gif)

![This is left join.](/images/Databases/img_leftjoin.gif "This is a sample image.")

![This is right join.](/images/Databases/img_rightjoin.gif)

![This is cross join.](/images/Databases/img_crossjoin.png)

=========================================

A **Database Transaction** is the a group of changes that is performed at the db on one go. If a transaction fails the database can be restore to its previous state.

**Properties of transactions: ACID** </br>

**A**tomicity - all changes successfully completed </br>

**C**onsistency - Changes are consistent with our db rules, constraints </br>

**I**solation - Transactions do not interfere with other transactions </br>

**D**urability - AFter the transaction completes and restart of system failure does not affect consistency of data. </br>


===================================  </br>

**Amazon RDS**- 6 Relational databases that Amazon supports </br>
* MySQL
* Amazon Aurora
* Microsoft SQL Server
* PostgreSQL
* MariaDB
* Oracle

</br>

**RDS is used when you need complex queries; otherwise noSQL** </br>

============================================ </br>

**Commonly Used MySQL Commands**
1. SELECT — extracts data from a database
SELECT column_name
FROM table_name;
SELECT statements fetch data from a database.
2. UPDATE — updates data in a database
UPDATE table_name
SET some_column = some_value
WHERE some_column = some_value;
UPDATE statements allow us to edit rows in a table.
3. DELETE — deletes data from a database
DELETE FROM table_name
WHERE some_column = some_value;
DELETE statements remove rows from a table.
4. INSERT INTO — inserts new data into a database
INSERT INTO table_name (column_1, column_2, column_3)
VALUES (value_1, ‘value_2’, value_3);
INSERT statements add a new row to a table.
5. CREATE DATABASE — creates a new database
CREATE DATABASE databasename;
CREATE DATABASE statements create a new SQL database.
6. ALTER DATABASE — modifies a database
ALTER DATABASE database_name
[COLLATE collation_name ]
ALTER DATABASE statements change the characteristics of a database.
7. CREATE TABLE — creates a new table
CREATE TABLE table_name (
column_1 datatype,
column_2 datatype,
column_3 datatype
);
CREATE TABLE statements create a new table in the database.
8. ALTER TABLE — modifies a table
ALTER TABLE table_name
ADD column_name datatype;
ALTER TABLE statements add, delete, or modify columns in an existing table.
9. DROP TABLE — deletes a table
DROP TABLE table_name;
DROP TABLE statements drop an existing table in a database.
10. CREATE INDEX — creates an index
CREATE INDEX index_name
ON table_name (column_name1, column_name2…);
Index statements create on existing tables to retrieve the rows quickly.
11. DROP INDEX — deletes an index
ALTER TABLE table_name
DROP INDEX index_name;
DROP INDEX statements delete an index in a table.


![SQL Cheatsheet](/images/Databases/sqlInNutShell.png) </br>

-----------------------------------------------= </br>

Some of the additional resources that I have worked on can be found below:

[Commands Used in the 162-DF-Lab](/DB_Files/DB_LastLab) </br>

[Connecting to MySQL in Ubuntu](/DB_Files/MySQL_in_Ubuntu ) </br>

----------------------------------------------- </br>


**Using Python with Postgres**  </br>

-----------------------------------------------    </br> 
> :memo: **Note:** Pip is the package manager for python. use psycopg2 module to connect to the Databases. To get the module -   
pip install psycopg2   </br> 

-----------------------------------------------   
   </br>   
   
**Connect to PostgreSQL from Python :**  

Arguments required to connect PostgreSQL database from Python.  </br>   

**Username**: The username you use to work with PostgreSQL, The default username for the PostgreSQL database is Postgres. But it is advised to create a user before you start using database. </br> 

**Password**: Password is given by the user at the time of installing the PostgreSQL. </br> 

**Host Name**: This is the server name or Ip address on which PostgreSQL is running. if you are running on localhost, then you can use localhost, or its IP, i.e., 127.0.0.0 </br> 

**Database Name**: Database name to which you want to connect. ex. </br> 

> :bulb: **Tip:** 
conn = psycopg2.connect(host = "localhost", dbname = "myDB", user = "myUserName", password = "myPwd", port = 5432) </br> 

</br>

**Python PostgreSQL SELECT query** </br>

-----------------------------------------------
* Define a PostgreSQL SELECT Query </br> 
* Prepare a SQL SELECT query to fetch rows from a table. You can select all or limited rows based on your need. If the where condition is used, then it decides the number of rows to fetch. </br> 
ex. SELECT col1, col2,…colnN FROM postgresql_table WHERE id = 5;. This will return row number 5.
* Get Cursor Object from Connection </br> 
* Next, use a connection.cursor() method to create a Psycopg2 cursor object. This method creates a new psycopg2.extensions.cursor object. </br> 
* Execute the SELECT query using a execute() method </br> 
* Execute the select query using the cursor.execute() method. </br> 
* Extract all rows from a result </br> 
* After successfully executing a Select operation, Use the fetchall() method of a cursor object to get all rows from a query result. it returns a list of rows. </br> 
*-* Iterate each row - Iterate a row list using a for loop and access each row individually (Access each row’s column data using a column name or index number.) </br> 
* Close the cursor object and database connection object </br> 
use cursor.close() and connection.clsoe() method to close open connections after your work completes. </br> 

**[Read data from a table - Postgres](/DB_Files/dbRead.py )** </br>

------------------------------------------------ </br>

**Python PostgreSQL INSERT into database Table** </br> 
* Establish a PostgreSQL database connection in Python. </br> 
* Define the Insert query. All you need to know is the table’s column details. </br> 
* Execute the INSERT query using cursor.execute(). In return, you will get the number of rows affected. </br> 
* After the successful execution of the query, commit your changes to the database. </br> 
* Close the cursor and PostgreSQL database connection. </br> 
* Most important, Catch SQL exceptions if any. </br> 

**[Insert Row Into a Table - Postgres ](/DB_Files/dbCreateInsert.py )** </br>

**Python PostgreSQL UPDATE a row** </br> 
* Establish a PostgreSQL database connection in Python. </br> 
* Define the UPDATE statement query to update the data of the PostgreSQL table. </br> 
* Execute the UPDATE query using a cursor.execute() </br> 
* Close the cursor and database connection. </br>

**[Update row in a table - Postgres](/DB_Files/dbUpdate.py )**

**Python PostgreSQL DELETE a row** </br> 
* Establish a PostgreSQL database connection in Python. </br> 
* Define the DLETE statement query to update the data of the PostgreSQL table. </br> 
* Execute the DELETE query using a cursor.execute() </br> 
* Close the cursor and database connection. </br>

**[Delete row from a table - Postgres](/DB_Files/dbDelete.py )**  </br>

---------------------------------------------------------<br>

**Additional Useful Resources:** </br>

https://www.postgresqltutorial.com/  <br>

https://www.postgresqltutorial.com/postgresql-python/  </br>

https://www.youtube.com/watch?v=qw--VYLpxG4  </br>

https://www.sqlshack.com/overview-of-sql-rank-functions/ </br>

https://www.youtube.com/watch?v=5-La_uSNkKU </br>


Book - The Language of SQL by Larry Rockoff





