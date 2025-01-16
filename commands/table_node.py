"""
commands/table_node.py

Defines a TableNode. Used by Table to store meta data about tables and the table root

Attributes
* table_name
* Root Row_node

"""

__author__ = "Peter Degen-Portnoy"
__copyright__ = "Copyright 2025, Peter Degen-Portnoy"
__license__ = "See LICENSE file"
__version__ = "0.0.1"

from commands import row_node

class TableNode:
    def __init__(self, table_name, table_definition):
        self.table_name = table_name
        self.table_definition = table_definition
        self.root = row_node.RowNode(None, None)


