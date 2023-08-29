#!/usr/bin/python3
""" Define a class Square """


class Square:
    def __init__(self, size=0):
        """
        Initializes an instance of the Square class.

        Args:
            size (int): Size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
            return the current square area
        """
        return self.__size ** 2

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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
