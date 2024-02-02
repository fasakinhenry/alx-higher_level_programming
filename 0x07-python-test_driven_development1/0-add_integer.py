#!/usr/bin/python3

"""Implementation of an integer addition function.
The fuction returns an interger which is the addition,
of the arguments passed into it.
"""


def add_integer(a, b=98):
    """Returns the addition of a and b.
    Floating point arguments are typecasred into integers.
    Raises:
        TypeError: if a or b is not an integer or a float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
