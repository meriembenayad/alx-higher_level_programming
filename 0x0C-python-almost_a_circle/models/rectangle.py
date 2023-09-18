#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """ A class that represents a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initialize a rectangle instance with the given attributes.
            Call the super class with id
            Args:
                width (int): width of rectangle
                height (int): height of rectangle
                x (int):
                y (int):
                id (int):
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Width Setter
            Args:
                value (int): value of width
            Raises:
                TypeError: message
                ValueError: message
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ Height Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Height setter
            Args:
                value (int): value of height
            Raises:
                TypeError: message
                ValueError: message
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ x Getter """
        return self.__x

    @x.setter
    def x(self, value):
        """
            x Setter
            Args:
                value (int): value of x
            Raises:
                TypeError: message
                ValueError: message
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ y Getter """
        return self.__y

    @y.setter
    def y(self, value):
        """
            y Setter
            Args:
                value (int): value of y
            Raises:
                TypeError: message
                ValueError: message
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ Returns area value of the rectangleinstance """
        return self.__width * self.__height

    def display(self):
        """ Prints in stdout the rectangle with '#' """
        for i in range(self.y):
            print("")

        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """ Returns a string representation of the rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
            Assigns an argument to each attribute
            Args:
                *args (int): arguments
                    - 1st argument should be the id attribute
                    - 2nd argument should be the width attribute
                    - 3rd argument should be the height attribute
                    - 4th argument should be the x attribute
                    - 5th argument should be the y attribute
                **kwargs (dict): key/value argument
        """
        attributes = ["id", "width", "height", "x", "y"]
        for i, arg in enumerate(args):
            setattr(self, attributes[i], arg)

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of Rectangle """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
