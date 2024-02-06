#!/usr/bin/python3
"""A function that appends a string at the end of a text file (utf-8)
And also returns the number of characters added.
"""


def append_write(filename="", text=""):
    """This function takes 2 arguments: filename and text.
    It returns the number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as file_opened:
        characters_added = file_opened.write(text)
        return (characters_added)
