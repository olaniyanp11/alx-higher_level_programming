#!/usr/bin/python3
"""
    a function that appends a string
"""


def append_write(filename="", text=""):
    """
        a function that appends a string to a file
    """
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
