#!/usr/bin/python3
"""A function that returns the list of avaliable attributes
and methods of an object.
"""


def lookup(obj):
    """This function returns the list of avaliable attributes
    and methods of an object passed as an argument to the function.
    Arguments:
        obj: (object)
    Returns:
        A list of avaliable attributes and methods.
    """
    return dir(obj)
