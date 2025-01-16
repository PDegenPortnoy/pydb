"""
commands/field.py

Contains a Field, which is used by TableDefinition to define a Table
"""

__author__ = "Peter Degen-Portnoy"
__copyright__ = "Copyright 2025, Peter Degen-Portnoy"
__license__ = "See LICENSE file"
__version__ = "0.0.1"

class Field:
    def __init__(self, name, size, data_type):
        self.name = name
        self.size = size
        self.type = data_type
