#!/usr/bin/python3
""" Define a class Square """


class Square:
    """ Square object """

    def __init__(self, size=0):
        """ Private instance attribute: size """
        """
            Initializes an instance of the Square class.
            Args:
                size (int): Size of the square. Defaults to 0.
            Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
        """
        self.__size = size
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        self.__size = size

    def area(self):
        """ return the current square area """
        return self.__size ** 2
