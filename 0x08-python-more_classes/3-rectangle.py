#!/usr/bin/python3
""" Define a class Rectangle """


class Rectangle:
    """ class Rectangle that defines a rectangle """

    def __init__(self, width=0, height=0):
        """ Method Instantiation the instance
            Args:
                width: width of the rectangle
                height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter for the private instance attribute width
            Method that returns the value of the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the private instance attribute width
            Method that define the width
            Args:
                value: width of the rectangle
            Raises:
                TypeError: width must be an integer
                ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Getter for the private instance attribute height
            Method that returns the value of the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the private instance attribute height
            Method that define the height
            Args:
                value: height of the rectangle
            Raises:
                TypeError: height must be an integer
                ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ Method that returns area of rectangle """
        return self.__width * self.__height

    """ ============================= """
    """ Private instance method: PERIMETER """

    def perimeter(self):
        """ Method thats returns perimeter of a rectangle
            if width or height is equal to 0, perimeter is equal to 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Method thats returns a string representation of the rectangle """
        string = ""
        if (self.__width == 0 or self.__height == 0):
            return ""

        for i in range(self.__height):
            string += "#" * self.__width
            if i < self.height - 1:
                string += "\n"
        return string
