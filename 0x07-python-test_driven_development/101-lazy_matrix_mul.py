#!/usr/bin/python3
"""
    Module that multiplies 2 matrices,
    Using module NumPy
"""
""" import module numpy """




import numpy as np
def lazy_matrix_mul(m_a, m_b):
    """
        Multiplies two matrices using the NumPy module.
        Args:
            m_a (list): First list of numbers
            m_b (list): Second list of numbers
        Returns:
            matrix of multiply m_a * m_b
        Raises:
            TypeError: if args not list or not list of lists
            ValueError: if list are empty
            TypeError: if an element int a list not int or float
                or row of the list not equal
                or m_a & m_b can't multiply
    """
    return np.matmul(m_a, m_b)
