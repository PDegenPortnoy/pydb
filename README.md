# pydb
Stupidly small and simple database written in Python

#  Introduction
I've been curious about how databases work at a fundamental level for a while. You know; what make a database tick? How does the data get stored, what is needed to support multiple tables? How do you parse and execute a SQL statement? 

Well, this is the start of a journey to see how far along this path I can get. I am also using Python because it's popular and I've not written anything this ambitious in Python before.

# Approach

I started using *Database Internals* by Alex Petrov (https://www.databass.dev) as my main source.  I've taken a look at [tinydb](https://github.com/msiemens/tinydb/tree/master) by Markus Siemens to see if this will give me a leg up.  However, tinydb is a No-SQL database and I'm interested in having a SQL interface. Finally though, I've come across [Let's Build A Simple Database](https://cstack.github.io/db_tutorial/parts/part1.html), which starts with the REPL and that seems like a very good place to start.

Following the latters approach, I am starting with a REPL and parsing commands directly. I'll eventually need a command parser. I'm doing this with objects because I've been working in OO for decades and it feels natrual. I expect a lot of refactoring. 😃 

# REPL

The REPL (Read, Eval, Print, Loop) will provide the foundation for starting on our SSASD (Stupidly Small and Simple Database). We'll need a main function that prints a prompt to the screen, reads the input and acts on it. 

To run the repl, use `./pydb.py` from the project root directory

# Commands

The Simple Database reference uses Sqlite, which uses a "." to indicate a meta command, such as `.table` or `.exit`. I don't think I want to do that. I would like to have a meta-table with table data so that one could do `SELECT * from db_tables` and `DESCRIBE <table_name>` to get table details from the meta-table. Therefore, the Commands module can be simpler than the reference, which processes meta commands and SQL commands differently. 

First implementation will be of a hard-coded table `default` with the following schema:

    | ID | Username       | email               |
    |____|________________|____________________ |
    | 1  | Peter          | peter@example.com   |

## Requirements
1. Insert (case-insentitive) will take 3 fields: ID, user\_name, email. 
1. Select will display the rows that were Inserted

### Next Steps
1. Define a size for a Field
1. Constrain data to the field size
1. Display the size of the field in the SELECT output
	1. In order to do this, I would like a dummy `Table.create()` that takes a `TableDefinition`. The `TableDefinition` contains the configuration information for each of the columns, called `Field`s. 
1. Persist changes (Create, Insert, Update) to disk

