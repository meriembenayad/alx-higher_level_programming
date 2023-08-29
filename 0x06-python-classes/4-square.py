#!/usr/bin/python3
""" Define a class Square """


class Square:
    def __init__(self, size=0):
        """
        intialize the square
        Args:
            size (int): The size of the square
        """
        self.__size = size

    def area(self):
        """
        return the current square area
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        Getter property for the size of the square.
        Retrieve the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter property for the size of the square

        Args:
            value (int): New size value for the square

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")
