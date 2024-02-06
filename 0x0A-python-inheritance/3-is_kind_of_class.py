#!/usr/bin/python3
"""A function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class
or otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """A function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class
    or otherwise False.
    Arguments:
        obj: The object to check with with the a_class.
        a_class: The class to compare against.
    Returns:
        True if obj is an instance of a specified class.
        False if obj is not an instance of a specified class.
    """
    if (isinstance(obj, a_class)):
        return True
    return False
