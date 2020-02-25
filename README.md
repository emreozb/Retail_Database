You can see the .drawio files in the "E-R Model and Relational Model" folder for E-R diagram 
and relational using the website (https://www.draw.io/). Also, I put the photos (.png) of E-R model
and relational model into the same folder in case you are not able to open .drawio files. 
The ER (Entity Relationship) diagram represents the model of Retail Store Management System. 
It shows all the visual entities of database tables and all their relations. It used structure data 
and to define the relationships between structured data groups of Retail Store Management System 
functionalities. The entities of Retail Store Management Systems are Supplier, Product, Customer, Stock,
Store, Invoice, Employee, Online_Acc. Relational tables are Contains, Cust_invoice, Generates, In_Stock,
Online_cust, Purchases, Supplies, Works.


You can find DDL and SQL queries in "DDL and Queries" folder;
Source file (.sql)
Microsoft SQL Server/Transact-SQL
Retail Database is a sample database of a retail store. This was created in an effort to build 
appropriate constraints and to emulate a functional retail store database. Microsoft’s SQL Server 2017 
and specifically SQL Server Management Studio were used, but efforts were made to have the DDL be as 
compatible with Oracle. To create the database, it’s tables and load the data please open up the .sql file
provided and execute the query in SQL Server Management Studio by finding the ‘execute’ button or using 
the default executing key ‘f5’. Please note option 1 within the file is uncommented and with every 
execution switches the database to ‘master’ then creates the ‘retail’ database and then defaults to use 
that database when loading in the data.This should be compatible with prior versions of Microsoft SQL Server. 


In the "Python DDL and GUI using SQlite" folder, you will see 2 different Python files which are 
SQLprojectDDL.py and SQLprojectGUI.py.  SQLprojectDDL.py is developed for creating tables and 
inserting values into the tables using SQLite. You will need Json files which include the data 
that would be inserted as the values into tables. I put 16 different Json files into "JsonFiles" 
folder to be used for 16 different tables. You are going to need them to run SQLprojectDDL.py file. 
SQLprojectGUI.py is developed for graphical user interface. You can easily add new values into 16 different
tables using the this GUI. Also, you can write SQL queries in text field under "Show Records" button.
When you click the button, you are going to get the data in a new pop up window using the query.

I attached a word file is named "RetailRelationSchema" as well. It shows what primary keys and foreign keys
are in our Retail Database.

I also added the SQLite database. If you would like to see the database with tables and data, 
you can look at it. 
