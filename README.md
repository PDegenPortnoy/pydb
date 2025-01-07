# pydb
Stupidly small and simple database written in Python

#  Introduction
I've been curious about how databases work at a fundamental level for a while. You know; what make a database tick? How does the data get stored, what is needed to support multiple tables? How do you parse and execute a SQL statement? 

Well, this is the start of a journey to see how far along this path I can get.

# Approach

I'm using *Database Internals* by Alex Petrov (https://www.databass.dev) as my main source.  I've taken a look at tinydb by Markus Siemens (https://github.com/msiemens/tinydb/tree/master) to see if this will give me a leg up.  However, tinydb is a No-SQL database and I'm interested in having a SQL interface. 

I think I'll start by implementing the Storage Engine. According to Petrov, the Storage Engine contains a few components:

- Transaction Manager -- Schedules transactions and keeps the database in a consisent state
- Lock Manager -- Locks the database objects for the running transactions
- Access Methods (Storage Structures) -- These manage access and organize data on disk
- Buffer Manager -- Caches data pages in memory
- Recovery Manager -- Maintains the operation log and restores the system state in case of a failure.

The cricital question is "What is the minimum need to support a single user accessing multiple tables?" 

# Storage Engine

Some working assumptions and requirements:
1. The database shall support a single user only
1. The database shall use row-oriented data layout
1. The database shall provide support for multiple tables
