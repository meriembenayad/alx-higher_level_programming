#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class that represents a square """

    def __init__(self, size, x=0, y=0, id=None):
        """
            Initialize a square instance with given attribute
            Call supper class with id, x, y, width, height
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Return a string representation of the square """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ Size Getter """
        return self.width

    @size.setter
    def size(self, value):
        """
            Size Setter
            Assign width and height with the same value
            Setter should have the same value validation as the Rectangle
            for width and heigh
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            Assigns an argument to each attribute
            Args:
                *args (int): arguments
                    - 1st argument should be the id attribute
                    - 2nd argument should be the size attribute
                    - 3th argument should be the x attribute
                    - 4th argument should be the y attribute
                **kwargs (dict): key/value argument
        """
        attributes = ["id", "size", "x", "y"]
        for i, arg in enumerate(args):
            setattr(self, attributes[i], arg)

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
