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

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns the string representation of the
        rectangle description: [Rectangle] <width>/<height>
        """
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
