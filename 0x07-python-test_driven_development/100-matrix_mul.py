#!/usr/bin/python3
"""
    Multiply 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
        Function that multiplies 2 matrices
        Args:
            m_a (list): First list of numbers
            m_b (list): Second list of numbers
        Return:
            matrix of multiply m_a * m_b
        Raises:
            TypeError: if args not list or not list of lists
            ValueError: if list are empty
            TypeError: if an element int a list not int or float
                or row of the list not equal
                or m_a & m_b can't multiply
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for list_a in m_a:
        if not isinstance(list_a, list):
            raise TypeError("m_a must be a list of lists")

    for list_b in m_b:
        if not isinstance(list_b, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    for list_a in m_a:
        for item_a in list_a:
            if not isinstance(item_a, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for list_b in m_b:
        for item_b in list_b:
            if not isinstance(item_b, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    row_length_a = len(m_a[0])
    for list_a in m_a:
        if len(list_a) != row_length_a:
            raise TypeError("each row of m_a must be of the same size")

    row_length_b = len(m_b[0])
    for list_b in m_b:
        if len(list_b) != row_length_b:
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for j in range(len(m_b[0]))] for i in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
