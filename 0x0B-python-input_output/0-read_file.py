#!/usr/bin/python3
"""write a function that reads a text file and prints it to stdout"""

def read_file(filename=""):
    """read a text file"""
    with open(filename, encoding="utf-8") as f:
        line = f.read()
        print(line, end="")
        f.close()
