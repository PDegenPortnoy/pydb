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

from commands.row import Row
from commands.row_node import RowNode
from commands.row_field import RowField
from commands.table_definition import TableDefinition
from commands.field import Field
from commands.table_node import TableNode

class Table:
    def __init__(self, ):
        self.table_definition = None
        self.name = None
        self.row_nodes = [] 
        self.root = RowNode(None, None)


    def create(self, table_name, the_table_definition):
        """
        Takes a table name and a dict with the table definition.
        The Command class uses the SQLParser to parse the user input
        The Command class invokes Table.create() with the table definition, which
        is an array of Fields. Fields are column_name, column_size (using default values currently),
        and column_type.
        """
        # print(f"Table.create() table_name: {table_name}, the_table_definition: {the_table_definition}")
        # for elem in the_table_definition:
        #     print(f"   elem.name: {elem.name}, elem.size: {elem.size}, elem.type: {elem.type}")

        self.name = table_name
        self.table_definition = TableDefinition(the_table_definition)
        return self
 

    def insert(self, user_input: str) -> None:
        """
        Expecting "INSERT INTO <table_name> (value1, value2, ...)"
        This Table class is the one with the correct table_name, so the work
        is to parse the the values and create RowFields for each one.
        Then add the RowFields to a Row and save the Row
        """
        fields = []
        for i, value in enumerate(user_input['values']):
            # Get the the details from the table_definition.fields
            fields = self.table_definition.fields
            field_name, field_size, field_type = fields[i]['name'], fields[i]['size'], fields[i]['type']
            print(f"Table.insert(). field_name: {field_name}, field_size: {field_size}, field_type: {field_type}")
            row_field = RowField(field_name, value)
            print(f"Table.insert(). row_field: {row_field.field_name}, {row_field.value}")
            fields.append(row_field)
        self._add_row(Row(fields))


    def select(self, user_input: str) -> None:
        """
        Uses the default table root
        """
        the_table = self._get_table_by_name('users') # TODO: This has to be parsed from input
        node = the_table.root

        # Use the table definition to print the names of the fields and an underbar
        header_row = ""
        column_definitions = self.table_definition
        for field in column_definitions.fields:
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
        for field in column_definitions.fields:
            divider_row += "|" + "-" * field['size']
        divider_row += "|"
        print(divider_row)
        while node.row != None:
            print(f"|{node.row.format_for_printing('id')}|{node.row.format_for_printing('user_name')}|{node.row.format_for_printing('email')}|")
            node = node.child_node



    def _add_row(self, row: Row) -> int:
        if self.root.child_node == None:
            leaf = self.root
        else:
            leaf = self._get_leaf(the_table)
        leaf.row = row
        leaf.child_node = RowNode(None, None)


    def _get_leaf(self, the_table) -> RowNode:
        node = self.root 
        while node.child_node != None:
            node = node.child_node
        return node


    def _get_table_by_name(self, table_name) -> str:
        return self.tables[0] # This is the default 'users' table


