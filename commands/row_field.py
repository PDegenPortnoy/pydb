"""
commands/row_field.py

Defines a field that gets used in a Row.
Attributes
* field name -- string 
* field size -- int
* field_type -- data type of the field, e.g. int, str
* value -- the value of the field in the row

Note: Not imposing limits on size of field name or field size

Design Note: Probably only need field_name and value. field_size and field_type
belong in the Table Definition.

"""

__author__ = "Peter Degen-Portnoy"
__copyright__ = "Copyright 2025, Peter Degen-Portnoy"
__license__ = "See LICENSE file"
__version__ = "0.0.1"

class RowField:
    def __init__(self, field_name, field_size, field_type, value = None):
        self.field_name = field_name
        self.field_size = field_size # belongs in Table Definition
        self.field_type = field_type # belongs in Table Definition
        self.value = value
