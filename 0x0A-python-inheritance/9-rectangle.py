#!/usr/bin/python3
"""
a class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
       Rectangle class
    """

    def __init__(self, width, height):
        """
            Instantiation of Rectangle
            Args:
                width (int): width of Rectangle
                height (int): height of Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
            Method that return area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
            Return the following rectangle description:
            [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
