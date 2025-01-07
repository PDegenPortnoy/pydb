#!/usr/bin/env python

"""
This is the main file for the REPL and the core of the database
"""

__author__ = "Peter Degen-Portnoy, aka 'PDP'"
__copyright__ = "Copyright 2025, PDP"
__license__ = "See LICENSE file"
__version__ = "0.0.1"

import sys

def main():
  while True:
    print(">> ", end = '')
    sys.stdout.flush()

    input = sys.stdin.readline().strip()
    print(f"Command was '{input}'")

    if input == 'exit':
      break

  print("Exiting...")


if __name__ == "__main__":
    main()
