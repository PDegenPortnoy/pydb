"""
commands/table.py

Represents a table. Has hard coded columns. Has flexible rows stored in a linked list
Contains a root node. If a node.child_node is None, the node is the leaf and the row is empty. 
When a new row is added, a child_node is created and the `row` field is populated with the new row. 
Then a new, empty Node is created. 
"""

__author__ = "Peter Degen-Portnoy"
__copyright__ = "Copyright 2025, Peter Degen-Portnoy"
__license__ = "See LICENSE file"
__version__ = "0.0.1"

from commands import row

class RowNode:
    def __init__(self, child_node, row):
        self.child_node = child_node
        self.row = row 


class Table:
    def __init__(self, table_name: str):
        self.table_name = table_name
        self.root = RowNode(None, None)


    def insert(self, user_input: str) -> None:
        """
        Expecting "insert <id> <user_name> <email>"
        """
        _, id, user_name, email = user_input.split()
        the_row = row.Row(id, user_name, email) 
        self._add_node(the_row)
        print(f"Added row with id: {the_row.get_id()}.")


    def select(self, user_input: str) -> None:
        """
        Uses the default table root
        """
        print("|  ID   |  name      |  email        |")
        print("|_______|____________|_______________|")
        node = self.root
        while node.row != None:
            print(f"|{node.row.format_id_for_printing('id')}| {node.row.user_name}  | {node.row.email} |")
            node = node.child_node



    def _add_node(self, row: row.Row) -> int:
        if self.root.child_node == None:
            leaf = self.root
        else:
            leaf = self._get_leaf()
        leaf.row = row
        leaf.child_node = RowNode(None, None)

    def _get_leaf(self) -> RowNode:
        node = self.root
        while node.child_node != None:
            node = node.child_node
        return node 


