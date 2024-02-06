#!/usr/bin/python3
"""A function that creates an Object from a JSON file."""
import json


def load_from_json_file(filename):
    """This creates an object from a JSON file
    Arguments: filename: string.
    Returns: the object loaded from the JSON file
    """
    with open(filename, 'r', encoding="utf-8") as file_opened:
        json_data = file_opened.read()
        return json.loads(json_data)
