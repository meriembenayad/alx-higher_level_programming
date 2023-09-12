#!/usr/bin/python3
"""
 a class Square that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle """

    def __init__(self, size):
        """
            Method that return size of Square
            Args:
                size (int): size of a square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
            Return area of a square
        """
        return self.__size ** 2
