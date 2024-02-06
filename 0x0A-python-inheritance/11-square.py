#!/usr/bin/python3
"""A Square class that inherits from
Rectangle class.
"""
RectangleClass = __import__("9-rectangle").Rectangle


class Square(RectangleClass):
    """Initializes a square class inherited from
    Rectangle class.
    """

    def __init__(self, size):
        "Initliazing square class"
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return (self.__size * self.__size)

    def __str__(self):
        """Returns the string representation of the
        rectangle description: [Rectangle] <width>/<height>
        """
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
