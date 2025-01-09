"""
tests/test_table.py

Tests for the Table class
"""

__author__ = "Peter Degen-Portnoy"
__copyright__ = "Copyright 2025, Peter Degen-Portnoy"
__license__ = "See LICENSE file"
__version__ = "0.0.1"

import unittest
import sys, os
sys.path.append(os.path.abspath(sys.path[0]) + '/../')
from commands import table


class TableTests(unittest.TestCase):
    def test_insert(self):
        the_table = table.Table('default')
        self.assertIsNone(the_table.root.child_node)
        self.assertIsNone(the_table.root.row)
        the_table.insert('insert 1 test test@email.com')
        self.assertIsNotNone(the_table.root.row)
        self.assertIsNotNone(the_table.root.child_node)
        self.assertEqual(the_table.root.row.id, '1')
        self.assertEqual(the_table.root.row.user_name, 'test')
        self.assertEqual(the_table.root.row.email, 'test@email.com')

if __name__ == '__main__':
    unittest.main()
