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
        return token_pattern.findall(self.query.upper()) # TODO: This capitalizes the user input too, which we do not want. Move the upper() call further down the chain


    def parse(self):
        if not self.tokens:
            raise ValueError("Empty query")

        token = self.tokens[0]
        if token == 'CREATE':
            return self.parse_create()   
        elif token == 'INSERT':
            return self.parse_insert()
        elif token == 'SELECT':
            return self.parse_select()
        elif token == 'EXIT':
            return {'type': 'EXIT'}
        else:
            raise ValueError(f"Unsupported SQL statement: {token}")


    def parse_create(self):
        """ CREATE TABLE <table_name> (col_name col_type, ...)
            Parses statement. Returns table name and dict of column names and type
        """
        if self.tokens[1] != 'TABLE':
            raise ValueError("Invalid CREATE statement: No TABLE keyword")

        table_name = self.tokens[2]
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


    def parse_insert(self):
        """ INSERT INTO <table_name> (value1, value2, ...)
            Parses Insert statement. Returns table name and an array of values to insert
        """
        if self.tokens[1] != 'INTO':
            raise ValueError("Invalid INSERT statement: No INTO keyword")
        
        table_name = self.tokens[2]
        values = {} 
        if self.tokens[3] != '(':
            raise ValueError("Malformed INSERT statement: no opening parenthsis")
        else:
            values_array = self.tokens[4:-1]
            print(f"values_array: {values_array}")
            values_string = ''.join(values_array)
            print(f"values_string: {values_string}")
            values_array = values_string.split(',')

        return{'type': 'INSERT', 'table': table_name, 'values': values_array}
