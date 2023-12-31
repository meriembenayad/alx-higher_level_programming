#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    """declare an class BaseGeometry"""

    def area(self):
        """
        Public instance method:

        Raise:
            Exception with message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function that validate a value
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
