"""
commands/commands.py

Receives commands and determines what to do with them
"""

__author__ = "Peter Degen-Portnoy"
__copyright__ = "Copyright 2025, Peter Degen-Portnoy"
__license__ = "See LICENSE file"
__version__ = "0.0.1"

import sys

class Commands:
    def process(self, user_input):
        print(f"Command was '{user_input}'")

        if user_input == 'exit':
            print("exiting...")
            sys.exit()

