#!/usr/bin/python3
"""function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix.

    args:
    matrix:must be a list of lists of integers or floats
    div: must be a number (integer or float)

    """
    errorText = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(errorText)
    if not isinstance(matrix, list):
        raise TypeError(errorText)
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(errorText)
        for item in lists:
            if type(item) is not int and type(item) is not float:
                raise TypeError(errorText)
    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(errorText)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in lists] for lists in matrix]
