#!/usr/bin/python3
"""append_write"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)
    Returns the number of characters add"""
    with open(filename, 'a') as file_object:
        return file_object.write(text)
