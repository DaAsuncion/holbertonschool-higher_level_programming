#!/usr/bin/python3
"""init"""

def read_file(filename=""):
    """read a text file"""
    with open(filename, encoding="utf-8") as f:
        line = f.read()
    print(line, end="")
    f.close()
