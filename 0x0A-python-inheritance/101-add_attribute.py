#!/usr/bin/python3
"""A function that adds a new attribute to an object.
if possible.
"""


def add_attribute(object, attribute, value):
    """A function that adds a new attribute to an object
    Arguments:
        object (dict): The object to add attribute to.
        attribute (str): The name of the attribute.
        value (str): The value of the attribute.
    Raises TypeError: If object cannot have new attribute.
    """

    if (not hasattr(object, "__dict__")):
        """Check if object is an instance of a class."""
        raise TypeError("can't add new attribute")

    setattr(object, attribute, value)
