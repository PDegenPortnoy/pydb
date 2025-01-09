"""
commands/commands.py

Receives commands and determines what to do with them
"""

__author__ = "Peter Degen-Portnoy"
__copyright__ = "Copyright 2025, Peter Degen-Portnoy"
__license__ = "See LICENSE file"
__version__ = "0.0.1"

import sys
from commands import table

class Command:
    def process(self, user_input: str):
        # print(f"Command was '{user_input}'")

        if user_input.lower() == 'exit':
            self.process_exit()
        elif user_input.lower().startswith('select'):
            self.process_select(user_input)
        elif user_input.lower().startswith('insert'):
            self.process_insert(user_input)
        else:
            self.process_unrecognized(user_input)

    def process_exit(self) -> None:
        print("exiting...")
        sys.exit()


    def process_select(self, user_input: str) -> None:
        print(f"processing SELECT statement: `{user_input}`")


    def process_insert(self, user_input: str) -> None:
        the_table = table.Table('default')
        the_table.insert(user_input)


    def process_unrecognized(self, user_input: str) -> None:
        print(f"Unrecognized command: `{user_input}`")

