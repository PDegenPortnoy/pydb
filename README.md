# pydb
Stupidly small and simple database written in Python

#  Introduction
I've been curious about how databases work at a fundamental level for a while. You know; what make a database tick? How does the data get stored, what is needed to support multiple tables? How do you parse and execute a SQL statement? 

Well, this is the start of a journey to see how far along this path I can get. I am also using Python because it's popular and I've not written anything this ambitious in Python before.

# Approach

I started using *Database Internals* by Alex Petrov (https://www.databass.dev) as my main source.  I've taken a look at tinydb by Markus Siemens (https://github.com/msiemens/tinydb/tree/master) to see if this will give me a leg up.  However, tinydb is a No-SQL database and I'm interested in having a SQL interface. Finally though, I've come across [Let's Build A Simple Database](https://cstack.github.io/db_tutorial/parts/part1.html), which starts with the REPL and that seems like a very good place to start.

# REPL

The REPL (Read, Eval, Print, Loop) will provide the foundation for starting on our SSASD (Stupidly Small and Simple Database). We'll need a main function that prints a prompt to the screen, reads the input and acts on it. 

To run the repl, use `python repl/repl.py` from the project root directory

