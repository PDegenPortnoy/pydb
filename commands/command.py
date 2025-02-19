"""
commands/commands.py

Receives commands and determines what to do with them
"""

__author__ = "Peter Degen-Portnoy"
__copyright__ = "Copyright 2025, Peter Degen-Portnoy"
__license__ = "See LICENSE file"
__version__ = "0.0.1"

import sys
from commands.table import Table
from commands.sql_parser import SQLParser
from commands.field import Field

class Command:
    def __init__(self):
        # TODO: create the system table that holds table metadata
        self.tables = []

    def process(self, user_input: str):
        command = SQLParser(user_input).parse()
        print(f"Command.process: command is {command}")
        
        if command['type'] == 'EXIT':
            self.process_exit()
        elif command['type'] == 'CREATE':
             self.process_create(command)
        elif command['type'] == 'INSERT':
            self.process_insert(command)
        elif command['type'] == 'SELECT':
            self.process_select(command)
        else:
            self.process_unrecognized(command)

    def process_exit(self) -> None:
        print("exiting...")
        sys.exit()


    def process_create(self, command: dict) -> None:
        fields = []
        print(f"process_create: command['columns']: {command['columns']}")
        for key, value in command['columns'].items():
            print(f"process_create. key: {key}, value: {value}")
            default_size, data_type = self.get_size_and_type(value)
            field = Field(key, default_size, data_type)
            fields.append(field)
        table = Table()
        table.create(command['table'], fields)
        self.tables.append(table)


    def process_select(self, command: dict) -> None:
        table = command['table']
        table = self.tables[0]
        table.select(command)


    def process_insert(self, command: dict) -> None:
        table = self.tables[0]
        table.insert(command)


    def process_unrecognized(self, user_input: str) -> None:
        print(f"Unrecognized command: `{user_input}`")


    def get_size_and_type(self, data_type_string: str) -> set:
        if data_type_string == 'INT':
            return 32, int
        elif data_type_string == 'STRING':
            return 32, str
        else:
            raise ValueError(f"Unknown data type, {data_type_string}")



