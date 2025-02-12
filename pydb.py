#!/usr/bin/env python

"""
main.py

Runs the REPL
"""

__author__ = "Peter Degen-Portnoy, aka 'PDP'"
__copyright__ = "Copyright 2025, PDP"
__license__ = "See LICENSE file"
__version__ = "0.0.1"

import sys
sys.path.append('../')
from repl.repl import REPL 

def main():
    REPL().run()

if __name__ == "__main__":
    main()

