#!/usr/bin/python3
"""A function that inserts a line of text to a file,
after each line containing specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a text after each lone containing
    specific string.
    Arguments:
    filename: (string): The name of the file.
    search_string: (string): The string to be searched for in the file.
    new_string: (string): The string to be inserted.
    """
    text_to_append = ''
    with open(filename, encoding="utf-8") as file_opened:
        for current_line in file_opened:
            text_to_append += current_line
            if (search_string in current_line):
                text_to_append += new_string
    # open the file and write the text to it.
    with open(filename, "w", encoding="utf-8") as file_opended2:
        file_opended2.write(text_to_append)
