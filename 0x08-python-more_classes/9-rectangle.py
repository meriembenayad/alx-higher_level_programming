#!/usr/bin/python3
""" Define a class Rectangle """


class Rectangle:
    """ class Rectangle that defines a rectangle
        Attributes:
            number_of_instances (int): number of instances
            print_symbol (any): symbol used for string representation
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Method Instantiation the instance
            Args:
                width: width of the rectangle
                height: height of the rectangle
        """
        self.width = width
        self.height = height

        """ Incremented during each new instance instantiation """
        Rectangle.number_of_instances += 1

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
            string += str(self.print_symbol) * self.__width
            if i < self.height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """ MEthod that returns a string representation of the rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Method that prints a message when an instance is deleted """
        """ Decremented during each instance deletion """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Static Method returns biggest rectangle based on Area
            Args:
                rect_1: 1st Rectangle
                rect_2: 2d Rectangle
            Raises:
                TypeError: if rect_1 is not an instance of Rectangle
                TypeError: if rect_2 is not an instance of Rectangle
            Return:
                The rectangle with the greater or equal Area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Class method that return a new Rectangle instance with:
            width == height == size
            Args:
                cls: class itself
                size: The size for both width and height
            Return:
                A new Rectangle instance with equal width and height
        """
        return cls(size, size)
