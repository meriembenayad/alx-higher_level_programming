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
                width (int): width of rectangle
                height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
