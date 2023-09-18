#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """ A class that represents a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initialize a rectangle instance with the given attributes.
            Call the super class with id
            Args:
                width (int): The width of the new Rectangle.
                height (int): The height of the new Rectangle.
                x (int): The x coordinate of the new Rectangle.
                y (int): The y coordinate of the new Rectangle.
                id (int): The identity of the new Rectangle.
            Raises:
                TypeError: If either of width or height is not an int.
                ValueError: If either of width or height <= 0.
                TypeError: If either of x or y is not an int.
                ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
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
        return self.width * self.height

    def display(self):
        """ Prints in stdout the rectangle with '#' """
        if self.width == 0 or self.height == 0:
            print("")
            return

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
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif k == "y":
                    self.y = value

    def to_dictionary(self):
        """ Returns the dictionary representation of Rectangle """
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
