#!/usr/bin/python3
def add_integer(a, b=89):
    """ Check if a & b are integers or float """
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
