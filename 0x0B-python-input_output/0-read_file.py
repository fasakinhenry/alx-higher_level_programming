#!/usr/bin/python3
"""A function that reads a text file (UTF-8)"""


def read_file(filename=""):
    """Takes an argument filename and prints the text file content."""
    with open(filename, encoding="utf-8") as openedfile:
        print(openedfile.read(), end="")
