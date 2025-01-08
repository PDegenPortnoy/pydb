#!/usr/bin/env python

"""
This is the main file for the REPL and the core of the database
"""

__author__ = "Peter Degen-Portnoy, aka 'PDP'"
__copyright__ = "Copyright 2025, PDP"
__license__ = "See LICENSE file"
__version__ = "0.0.1"

import sys
from commands import Commands

class REPL:
    def run():
        while True:
            repl = REPL()
            repl.print_prompt()
            user_input = sys.stdin.readline().strip()
            Commands().process(user_input)
    

    def print_prompt(self):
        print(">> ", end = '')
        sys.stdout.flush()
