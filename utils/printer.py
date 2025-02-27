"""
utils/printer.py

Responsible for (ideally) all output to the screen

Starting with the support for printing the SELECT statement
"""

__author__ = "Peter Degen-Portnoy"
__copyright__ = "Copyright 2025, Peter Degen-Portnoy"
__license__ = "See LICENSE file"
__version__ = "0.0.1"

from commands.table import Table
from commands.row import Row

class Printer:
    def print_header(table):
        header_row = ""
        for field in table.table_definition.fields:
            # print(f"Printer.print_header. field: {field}")
            name_length = len(field['name'])
            col_size = field['size']
            padding = (col_size - name_length) // 2 # assumes the name with fit in the size
            header_row += "|" + " " * padding
            header_row += f"{field['name']}"
            header_row += " " * padding
            if (col_size - name_length) % 2 != 0:
                header_row += " "
        header_row += "|"
        print(header_row)
    
        divider_row = ""
        for field in table.table_definition.fields:
            divider_row += "|" + "-" * field['size']
        divider_row += "|"
        print(divider_row)
        

    def print_row(table, row):
        # Get the field size from the Table for each RowField
        row_string = '|'
        for row_field in row.row_fields:
            table_field = table.get_field_by_name(row_field.field_name)
            value_size = len(str(row_field.value))
            padding_size = (int(table_field['size']) - value_size) // 2
            row_string += ' ' * padding_size
            row_string += str(row_field.value)
            row_string += ' ' * padding_size
            if (int(table_field['size']) - value_size) %2 != 0:
                row_string += ' '
            row_string += '|'
        print(row_string)
