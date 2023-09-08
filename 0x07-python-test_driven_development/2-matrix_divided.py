#!/usr/bin/python3
""" Module that divide all elements of a matrix """


def matrix_divided(matrix, div):
    """
        Divide all elements of a matrix.
        Args:
            matrix (list): list of numbers
            div (int): number
        Return:
            new matrix
        Raises:
            TypeError: specify msg depends the case
            ZeroDivisionError: division by zero
    """
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for col in row:
            if not isinstance(col, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) \
                        of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for col in row:
            new_row.append(round(col / div, 2))

        new_matrix.append(new_row)

    return new_matrix
