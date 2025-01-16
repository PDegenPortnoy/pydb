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

from commands import row, row_node, table_definition, field, table_node
class Table:
    def __init__(self, ):
        self.tables = []
        self.create('users', None)


    def create(self, table_name, the_table_definition):
        # Hack to auto-define the Users table
        id_field = field.Field("id", 7, int)
        user_name_field = field.Field("user_name", 16, str)
        email_field = field.Field("email", 32, str)
        the_table_definition = table_definition.TableDefinition(
                                id_field,
                                user_name_field,
                                email_field,
                                )
        self.tables.append(table_node.TableNode('users', the_table_definition))
        

    def insert(self, user_input: str) -> None:
        """
        Expecting "insert <id> <user_name> <email>"
        """
        _, id, user_name, email = user_input.split()
        users_table = self._get_table_by_name('users')
        the_row = row.Row(id, user_name, email) 
        self._add_node('users', the_row)
        print(f"Added row with id: {the_row.get_id()}.")


    def select(self, user_input: str) -> None:
        """
        Uses the default table root
        """
        print("|  ID   |    name    |    email      |")
        print("|_______|____________|_______________|")
        the_table = self._get_table_by_name('users') # TODO: This has to be parsed from input
        node = the_table.root
        while node.row != None:
            print(f"|{node.row.format_id_for_printing('id')}| {node.row.user_name}  | {node.row.email} |")
            node = node.child_node



    def _add_node(self, table_name, row: row.Row) -> int:
        the_table = self._get_table_by_name(table_name)
        if the_table.root.child_node == None:
            leaf = the_table.root
        else:
            leaf = self._get_leaf(the_table)
        leaf.row = row
        leaf.child_node = row_node.RowNode(None, None)

    def _get_leaf(self, the_table) -> row_node.RowNode:
        node = the_table.root 
        while node.child_node != None:
            node = node.child_node
        return node


    def _get_table_by_name(self, table_name) -> str:
        return self.tables[0] # This is the default 'users' table


