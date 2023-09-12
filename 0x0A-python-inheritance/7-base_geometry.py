#!/usr/bin/python3
"""
a class BaseGeometry
"""


class BaseGeometry:
    """ BaseGeometry class """

    def area(self):
        """
            Public instance method
            Raise:
                Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            method that validates value
            Args:
                name (str): name of the value to be validate
                value (int): integer to be validate
            Raises:
                TypeError: If value is not an integer.
                ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
