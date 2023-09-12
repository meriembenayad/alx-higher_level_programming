#!/usr/bin/python3
"""
function that adds a new attribute
to an object if it's possible
"""


def add_attribute(obj, attr, value):
    """
        function that adds a new attribute to an object
        Args:
            obj (any): the object that the attribute added to
            attr (str): the name of the added attribute
            value (any): the value of attribute
        Raise:
            TypeError: if the object can’t have new attribute
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
