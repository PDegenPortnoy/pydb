"""
This is the main file for the REPL and the core of the database
"""

__author__ = "Peter Degen-Portnoy, aka 'PDP'"
__copyright__ = "Copyright 2025, PDP"
__license__ = "See LICENSE file"
__version__ = "0.0.1"

import sys
from commands import command

class REPL:
    def run() -> None:
        """
        The 'while' loop for the REPL
        """
        while True:
            REPL().print_prompt()
            user_input = sys.stdin.readline().strip()
            commander = command.Command()
            commander.process(user_input)
    

    def print_prompt(self) -> None:
        """
        Prints the command prompt.
        """
        print("db: ", end = '')
        sys.stdout.flush()
