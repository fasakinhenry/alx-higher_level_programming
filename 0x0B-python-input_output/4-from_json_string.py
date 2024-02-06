#!/usr/bin/python3
"""A function that returns an object (Python Data Structure),
Represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """This function returns a python object.
    Arguments: my_str which is JSON.
    Returns: an object (Python Data Structure).
    """
    return json.loads(my_str)
