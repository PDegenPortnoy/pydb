"""
commands/row.py

Defines a single Row. Rows are owned by a "RowNode", which is a node in a linkedList.
"""

__author__ = "Peter Degen-Portnoy"
__copyright__ = "Copyright 2025, Peter Degen-Portnoy"
__license__ = "See LICENSE file"
__version__ = "0.0.1"

class Row:
    def __init__(self, id: int, user_name: str, email: str):
        self.id = id
        self.user_name = user_name
        self.email = email

    def format_id_for_printing(self):
        #TODO This will need to take in the name of the RowField
        # the RowField will define the field size
        print_string = f"  {self.id}   "
        return print_string
