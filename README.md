# Overview
I developed a financial tracker software to further enhance my skills in programming with SQL databases as a computer engineer. The program is designed to help users record and manage their expenses and income, providing data into their financial activities. The software integrates with a SQLite relational database, offering a structured and efficient way to store and retrieve the financial data.

The purpose of creating this program is to gain hands-on experience in building applications that interact with databases. It serves as a practical exercixe to reinforce my understanding of SQL databases and their integration with software applications.

[Expense Tracker Demo Video]()

# Relational Database
The financial tracker utilizes a SQLite relational database to store information about expenses and income. The database consists of two tables which are expenses and income.
<br>
Table Structure for Expenses:
* 'id' (INTEGER): Primary key for expense entries
* 'amount' (REAL): The amount of the expense
* 'description' (TEXT): A brief description of the expense
* 'date' (TEXT): Timestamp indicating when the expense was recorded


Table Structure for Income:
* 'id' (INTEGER): Primary key for expense entries
* 'amount' (REAL): The amount of the expense
* 'description' (TEXT): A brief description of the expense
* 'date' (TEXT): Timestamp indicating when the expense was recorded

# Development Environment
The software was designed using the following tools and technologies:
* Programming Language - Python
* Database - SQLite3
* Integrated Development Environment - Visual Studio Code
* Libraries - datetime & SQLite3

# Useful Websites
1. [Python SQLite Tutorial by Corey Schafer](https://www.youtube.com/watch?v=pd-0G0MigUA)
2. [SQLite Documentation](https://www.sqlite.org/docs.html)
3. [SQL Tutorials by W3Schools](https://www.w3schools.com/sql/)

# Future Work
1. Implement user authentication to secure financial data
2. Add the ability to edit and delete individual expenes and/or income entries
3. Create an option to dispaly financial data with graphs
