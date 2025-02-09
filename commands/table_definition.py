"""
commands/table_definition.py

Contains the TableDefinition, which is the details about the definition of the table.
Identifies the fields and their attributes

"""

__author__ = "Peter Degen-Portnoy"
__copyright__ = "Copyright 2025, Peter Degen-Portnoy"
__license__ = "See LICENSE file"
__version__ = "0.0.1"

class TableDefinition:
    def __init__(self, *column_definitions):
        self.fields = []
        for c_d in column_definitions: 
            column = {}
            column['name'] = c_d.name
            column['size'] = c_d.size
            column['type'] = c_d.type
            self.fields.append(column)
