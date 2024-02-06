#!/usr/bin/python3
"""A function that returns the JSON representation of a string."""
import json


def to_json_string(my_obj):
    """This function returns the JSON representation of a string.
    Arguments: my_obj, which is valid Object.
    Returns: a JSON string representation of that object.
    """
    return json.dumps(my_obj)
