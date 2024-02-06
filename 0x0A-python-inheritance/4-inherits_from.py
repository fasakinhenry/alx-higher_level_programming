#!/usr/bin/python3
"""A function that Checks if an object is an inherited instance of a class"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.
    Arguments:
        obj: The object to check. , a_class: The class to compare against.

    Returns:
        True if the object is an instance that inherited.
        (directly or indirectly) from the specified class.
        of the class else False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
