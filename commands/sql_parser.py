"""
commands/sql_parser.py

Parse input from the command line
"""

__author__ = "Peter Degen-Portnoy"
__copyright__ = "Copyright 2025, Peter Degen-Portnoy"
__license__ = "See LICENSE file"
__version__ = "0.0.1"

import re


class SQLParser:
    def __init__(self, query):
        self.query = query.strip()
        self.tokens = self.tokenize()


    def tokenize(self):
        """ Split query into tokens """
        token_pattern = re.compile(r'\w+|[().,@=*]')
        return token_pattern.findall(self.query) # TODO: This capitalizes the user input too, which we do not want. Move the upper() call further down the chain


    def parse(self):
        if not self.tokens:
            raise ValueError("Empty query")

        token = self.tokens[0]
        if token.upper() == 'CREATE':
            return self.parse_create()   
        elif token.upper() == 'INSERT':
            return self.parse_insert()
        elif token.upper() == 'SELECT':
            return self.parse_select()
        elif token.upper() == 'DELETE':
            return self.parse_delete()
        elif token.upper() == 'EXIT':
            return {'type': 'EXIT'}
        else:
            raise ValueError(f"Unsupported SQL statement: {token.upper()}")


    def parse_create(self) -> dict:
        """ CREATE TABLE <table_name> (col_name col_type, ...)
            Parses statement. Returns table name and dict of column names and type
        """
        if self.tokens[1].upper() != 'TABLE':
            raise ValueError("Invalid CREATE statement: No TABLE keyword")

        table_name = self.tokens[2].upper()
        columns = {}
        if self.tokens[3] != '(':
            raise ValueError("Malformed CREATE statement: no opening parenthesis")
        else:
            i = 4
            while i < len(self.tokens) and self.tokens[i] != ')':
                columns[self.tokens[i]] = self.tokens[i+1]
                i += 2
                if self.tokens[i] == ',':
                    i += 1
            if i == len(self.tokens) or self.tokens[i] != ')': # TODO: should this be an "and"? Do we need the first part of the conditional? How does it help?
                raise ValueError("Malformed CREATE Statement: no closing parenthesis")

        return {'type': 'CREATE', 'table': table_name, 'columns': columns}


    def parse_insert(self) -> dict:
        """ INSERT INTO <table_name> (value1, value2, ...)
            Parses Insert statement. Returns table name and an array of values to insert
        """
        if self.tokens[1].upper() != 'INTO':
            raise ValueError("Invalid INSERT statement: No INTO keyword")
        
        table_name = self.tokens[2].upper()
        values = {} 
        if self.tokens[3] != '(':
            raise ValueError("Malformed INSERT statement: no opening parenthsis")
        else:
            # TODO: Need to parse these much more carefully to make sure we haven't lost spaces or changed capitalization. 
            # Need the original query, which is stored in self.query
            values_array = self.tokens[4:-1]
            values_string = ''.join(values_array) # TODO: This looses spaces in values
            values_array = values_string.split(',')

        return{'type': 'INSERT', 'table': table_name, 'values': values_array}


    def parse_select(self) -> dict:
        """ SELECT * FROM <table_name>
            Parses Select statement. Doesn't handle filtering by column names yet
        """
        if self.tokens[1] != "*":
            raise ValueError("Invalid SELECT statement: only handles SELECT *")
        elif self.tokens[2].upper() != "FROM":
            raise ValueError("Invalid SELECT statement: missing FROM")

        table_name = self.tokens[3].upper()
        return{'type': 'SELECT', 'table': table_name, 'columns': '*'}


    def parse_delete(self) -> dict:
        """ DELETE FROM <table_name> where <field> = <value>
            Deletes all the records that match the given condition
        """
        if self.tokens[1].upper() != 'FROM':
            raise ValueError("Invalid DELETE statement: missing FROM")
        if self.tokens[3].upper() != 'WHERE':
            raise ValueError("Invalid DELETE statement: missing WHERE")
        if self.tokens[5] != '=':
            raise ValueError("Invalid DELETE statement: missing =")

        table_name = self.tokens[2].upper()
        field, value = self.tokens[4].upper(), self.tokens[6]
        condition = {field: value}
        
        return{'type': 'DELETE', 'table': table_name, 'condition': condition}
        
