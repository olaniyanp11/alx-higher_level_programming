#!/usr/bin/python3
"""
    writes an Object to a text file, using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """
        a  function that writes an Object
        to a text file, using a JSON representation:
    """
    dumped = json.dumps(my_obj)
    with open(filename, "w") as f:
        f.write(dumped)
