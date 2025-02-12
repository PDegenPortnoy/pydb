# pydb
Small and simple database written in Python

#  Introduction
I've been curious about how databases work at a fundamental level for a while. You know; what make a database tick? How does the data get stored, what is needed to support multiple tables? How do you parse and execute a SQL statement? 

Well, this is the start of a journey to see how far along this path I can get. I am also using Python because it's popular and I've not written anything this ambitious in Python before.

# Approach

I started using *[Database Internals](https://www.databass.dev)* by Alex Petrov as my main source. But starting from the Binary Tree / B-Tree / B-Tree+ level seemed like missing the point of understanding the higher order operations. It may be necessary to get all the way to the point of managing disk storage that concretely. It may require writing a C module.

I then looked at [tinydb](https://github.com/msiemens/tinydb/tree/master) by Markus Siemens to see if this would give me a leg up.  However, tinydb is a No-SQL database and I'm interested in having a SQL interface. 

Finally though, I've come across [Let's Build A Simple Database](https://cstack.github.io/db_tutorial/parts/part1.html), which starts with the REPL and that seems like a very good place to start.

Following the "Let's Build A Simple Database" approach, I am starting with a REPL and parsing commands directly.

I'll eventually need a command parser. I'm doing this with objects because I've been working in OO for decades and it feels natural. I expect a lot of refactoring. 😃

# REPL

The REPL (Read, Eval, Print, Loop) will provide the foundation for starting on our database. We'll need a main function that prints a prompt to the screen, reads the input and acts on it. 

To run the repl, use `./pydb.py` from the project root directory

# Commands

The Simple Database reference uses Sqlite, which uses a "." to indicate a meta command, such as `.table` or `.exit`. I don't think I want to do that. I would like to have a meta-table with table data so that one could do `SELECT * from db_tables` and `DESCRIBE <table_name>` to get table details from the meta-table. Therefore, the Commands module can be simpler than the reference, which processes meta commands and SQL commands differently. 

First implementation will be of a hard-coded table `default` with the following schema:

    | ID | Username       | email               |
    |____|________________|____________________ |
    | 1  | Peter          | peter@example.com   |

## Requirements
1. CREATE <table_name> (<column_name> <column_type>, ...) will create a table with the define table attributes
1. INSERT INTO <table_name> (<column_name1>, ...) VALUES (<value1>, ...) will insert a record into the table with the provided values
1. SELECT * FROM <table_name> will select all the records from the table listed

### Current Functionality
Note: no punctuation. Currently displays a "db: " prompt and accepts the commands indicated below. The table is now defined at creation in the Table class. (That needs to be moved to the user.) Display uses the RowField attributes to display the row field value.

Usage:

1. insert ID Name Email
1. select 
1. exit


### Next Steps
1. Define a size for a Field in Table Create (Done)
1. Build a SQL Parser to parse CREATE, INSERT, and SELECT statements
1. Constrain data to the field size
1. Display the size of the field in the SELECT output
	1. In order to do this, I would like a dummy `Table.create()` that takes a `TableDefinition`. The `TableDefinition` contains the configuration information for each of the columns, called `Field`s. 
1. Persist changes (Create, Insert, Update) to disk

# 
