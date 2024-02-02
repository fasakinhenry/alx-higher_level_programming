#!/usr/bin/python3
"""A function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix
    Arguments:
        (matrix) : an array
        (div): an integer
    """
    
    if (not matrix and matrix is None and matrix is  [[]]):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if (len(row) is not len(matrix[0])):
            raise TypeError("Each row of the matrix must have the same size")
        else:
            for element in row:
                if (type(element) is not int and type(element) is not float or type(row) is not list ):
                    raise TypeError(
                        "matrix must be a matrix (list of lists) of integers/floats")
    if (type(div) is not int and type(div) is not float):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda num: round(num / div, 2), row)) for row in matrix])
