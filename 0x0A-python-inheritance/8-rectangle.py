#!/usr/bin/python3
"""A class that inherits from BaseGeometry class."""
BaseGeometryClass = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometryClass):
    """A class that inherits from BaseGeometry class."""

    def __init__(self, width, height):
        """Init a new Rectangle object
        Arguments:
            (width): integer, the width of the rectangle
            (height): integer, the height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
