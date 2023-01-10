#!/usr/bin/python3
"""
    a function that appends a string 
"""


def append_write(filename="", text=""):
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
