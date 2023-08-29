#!/usr/bin/python3
"""
Define a class Square
"""


class Square:
    """
    Private instance attribute: size
    """

    def __init__(self, size):
        """
            Initializes a square with the given size.

            Args:
                size (int): Size of the square.
        """
        self.__size = size
