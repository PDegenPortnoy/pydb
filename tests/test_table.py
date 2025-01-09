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
import commands.table

class TableTests(unittest.TestCase):
    def test_insert(self):
        table = Table('default')
        self.assertEqual(table.root.child_node, None)

if __name__ == '__main__':
    unittest.main()
