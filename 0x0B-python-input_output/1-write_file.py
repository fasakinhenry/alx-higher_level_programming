#!/usr/bin/python3
"""A function that writes a string to text file (utf-8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """This functions takes a filename and a text string to write to
    the specified file. It also returns the number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as file_opened:
        char_written = file_opened.write(text)
        return (char_written)
