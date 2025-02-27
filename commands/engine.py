"""
commands/engine.py

Receives commands and determines what to do with them
"""

__author__ = "Peter Degen-Portnoy"
__copyright__ = "Copyright 2025, Peter Degen-Portnoy"
__license__ = "See LICENSE file"
__version__ = "0.0.1"

import sys
from commands.table import Table
from commands.table_node import TableNode
from commands.sql_parser import SQLParser
from commands.field import Field
from utils.printer import Printer

class TableNotFoundError(Exception):
    pass

class Engine:
    def __init__(self):
        # TODO: create the system table that holds table metadata
        self.tables = []

    def process(self, user_input: str):
        command = SQLParser(user_input).parse()
        # print(f"Engine.process: command is {command}")
        
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
        # print(f"process_create: command['columns']: {command['columns']}")
        for key, value in command['columns'].items():
            # print(f"process_create. key: {key}, value: {value}")
            default_size, data_type = self.get_size_and_type(value)
            field = Field(key, default_size, data_type)
            fields.append(field)
        table = Table()
        table = table.create(command['table'], fields)
        self.tables.append(table)
        # self._show_tables()
        print(f"Created table '{command['table']}'")


    def process_insert(self, command: dict) -> None:
        # print(f"Engine.process_insert() command: {command}")
        table = self._find_table(command['table'])
        table.insert(command)
        print("Inserted record")


    def process_select(self, command: dict) -> None:
        table = self._find_table(command['table'])
        results = table.select(command) # Note: This works only for result sets up to a certain size
        Printer.print_header(table)
        for row in results:
            Printer.print_row(table, row)


    def process_unrecognized(self, user_input: str) -> None:
        print(f"Unrecognized command: `{user_input}`")


    def get_size_and_type(self, data_type_string: str) -> set:
        if data_type_string == 'INT':
            return 32, int
        elif data_type_string == 'STRING':
            return 32, str
        else:
            raise ValueError(f"Unknown data type, {data_type_string}")


    def _find_table(self, table_name: str) -> Table:
        for table in self.tables:
            if table.name == table_name:
                return table
        raise TableNotFoundError(f"Could not find table '{table_name}'")


    def _show_tables(self):
        for table in self.tables:
            print(f"Table: {table.name}, number of rows: {table.number_rows()}")
            for field in table.table_definition.fields:
                print(f"  name: {field['name']}, size: {field['size']}, type: {field['type']}")

