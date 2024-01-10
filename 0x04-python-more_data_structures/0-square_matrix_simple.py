#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix == []:
        return matrix
    new = [[x**2 for x in i] for i in matrix]
    return new
