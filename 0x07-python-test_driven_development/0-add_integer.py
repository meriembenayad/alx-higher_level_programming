#!/usr/bin/python3
"""
    This module define by:
    add_integer
    to: Adds two numbers.
"""


def add_integer(a, b=98):
    """ This is a multi-line docstring
        this is method for:
        Check if a & b are integers or float """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")

    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    """ Cast a and b to int if they are float """
    if (isinstance(a, float)):
        a = int(a)

    if (isinstance(b, float)):
        b = int(b)

    """ Return: sum of a + b """
    return (a + b)
