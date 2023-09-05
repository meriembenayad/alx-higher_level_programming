#!/usr/bin/python3
"""
    Module that prints a square with '#' character
"""


def print_square(size):
    """
        Prints square with # character
        Args:
            size (int): lenght of the square
        Return:
            Square with '#'
        Raises:
            TypeError: if size not int or less than 0
            ValueError: if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
