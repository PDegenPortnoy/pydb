"""
commands/table_definition.py

Contains the TableDefinition, which is the details about the definition of the table.
Identifies the fields and their attributes

"""

__author__ = "Peter Degen-Portnoy"
__copyright__ = "Copyright 2025, Peter Degen-Portnoy"
__license__ = "See LICENSE file"
__version__ = "0.0.1"

from commands.field import Field

class TableDefinition:
    def __init__(self, column_definitions):
        # print(f"TableDefinition.__init__(): column_definitions: {column_definitions}")
        self.fields = []
        for col in column_definitions: 
            # print(f"   col.name: {col.name}, col_size: {col.size}, col.type: {col.type}")
            column = {}
            column['name'] = col.name
            column['size'] = col.size
            column['type'] = col.type
            self.fields.append(column)
