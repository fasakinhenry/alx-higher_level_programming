#!/usr/bin/python3

# Removes all characters 'c' and 'C' from a string.
def no_c(my_string):
    result = ""
    for char in my_string:
        if char.lower() not in ('c', 'C'):
            result += char
    return result
