#!/usr/bin/python3
"""
a class Square that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size):
        """
            Instantiation of Square
            Args:
                size (int): size of Square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Return size of a square """
        return self.__size ** 2

    def __str__(self):
        """
            Return the following rectangle description:
            [Rectangle] <width>/<height>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
