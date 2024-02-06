#!/usr/bin/python3
"""A function that writes an Object to a text file,
Using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """This function writes JSON to text file.
    Arguments: my_obj: string, filename: string
    """
    with open(filename, 'w', encoding="utf-8") as file_opened:
        file_opened.write(json.dumps(my_obj))
