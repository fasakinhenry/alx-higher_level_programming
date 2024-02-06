#!/usr/bin/python3
"""A BaseGeometry class based on previous task
public instance method: area(self)
"""


class BaseGeometry:
    """An empty Base Geometry Class.
    Arguments: self
    Returns: null
    """

    def __init__(self):
        pass

    def area(self):
        """An empty Base Geometry Class.
        Arguments: self
        Returns: null
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator function."""
        if (type(value) != int):
            raise TypeError("{:s} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(name))
