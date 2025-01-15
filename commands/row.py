"""
commands/row.py

Defines a single Row. Rows are owned by a "RowNode", which is a node in a linkedList.
"""

__author__ = "Peter Degen-Portnoy"
__copyright__ = "Copyright 2025, Peter Degen-Portnoy"
__license__ = "See LICENSE file"
__version__ = "0.0.1"

from commands import row_field

class Row:
    def __init__(self, id: int, user_name: str, email: str):
        self.id = row_field.RowField(
                    field_name = 'id',
                    field_size = 7, 
                    field_type = int,
                    value = id,
                    )
        self.user_name = user_name
        self.email = email

    def get_id(self):
        return self.id.value

    def format_id_for_printing(self, field_name):
        row_field = self._get_field_by_name(field_name)
        ret_val = ""
        value_size = len(str(row_field.value)) 
        padding_size = (row_field.field_size - value_size) // 2
        # print(f"*** padding_size: {padding_size}, value_size: {value_size}, field_size: {row_field.field_size}")
        ret_val += ' ' * padding_size
        ret_val += str(row_field.value)
        ret_val += ' ' * padding_size
        return ret_val
            
            
        print_string = f"  {self.id}   "
        return print_string


    def _get_field_by_name(self, field_name):
        return self.id  
