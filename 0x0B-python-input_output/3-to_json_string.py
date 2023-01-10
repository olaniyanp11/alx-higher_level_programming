#!/usr/bin/python3
import json
"""
     function that returns the JSON representation of an object
"""


def to_json_string(my_obj):
    """
        returns json representation of my_obj
    """
    return json.dumps(my_obj)
