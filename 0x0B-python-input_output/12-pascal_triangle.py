#!/usr/bin/python3
"""A function that returns a list of integers representing the
Pascal's Triangle
"""


def pascal_triangle(n):
    """Returns a list of integers representing the pascal's triangle
    Arguments: n: integer
    Retuns: a list of integers representing Pascal's triangle.
    """
    pascal_triangle = []
    if (n <= 0):
        return pascal_triangle
    for i in range(n):
        if (i == 0):
            pascal_triangle.append([1])
        else:
            previous_row = pascal_triangle[i - 1]
            # this is a constant row
            row = [1]
            for j in range(1, i):
                row.append(previous_row[j - 1] + previous_row[j])
            row.append(1)
            pascal_triangle.append(row)
    return pascal_triangle
