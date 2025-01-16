"""
commands/row.py

Defines a single Row. Rows are owned by a "RowNode", which is a node in a linkedList.
Rows are comprised of RowFields, which own the attributes of field name, field size,
field type, and the actual value of the field

"""

__author__ = "Peter Degen-Portnoy"
__copyright__ = "Copyright 2025, Peter Degen-Portnoy"
__license__ = "See LICENSE file"
__version__ = "0.0.1"

from commands import row_field

class Row:
    def __init__(self, *row_fields: [row_field.RowField]):
        self.row_fields = []
        for rf in row_fields:
            field = row_field.RowField(
                        rf.field_name,
                        rf.field_size,
                        rf.field_type,
                        rf.value,
                        )
            self.row_fields.append(field)


    def get_id(self):
        for rf in self.row_fields:
            if rf.field_name == 'id':
                return rf.value
        return '-'

    def format_for_printing(self, field_name):
        row_field = self._get_field_by_name(field_name)
        ret_val = ""
        value_size = len(str(row_field.value)) 
        padding_size = (row_field.field_size - value_size) // 2
        # print(f"*** padding_size: {padding_size}, value_size: {value_size}, field_size: {row_field.field_size}")
        ret_val += ' ' * padding_size
        ret_val += str(row_field.value)
        ret_val += ' ' * padding_size
        if (row_field.field_size - value_size) % 2 != 0:
            ret_val += ' '
        return ret_val
            
    def _get_field_by_name(self, field_name):
        for row_field in self.row_fields:
            if row_field.field_name == field_name:
                return row_field
        raise NameError(f"'{field_name}' not found")
