#!/usr/bin/python3
"""
Write a function that returns:
True if the object is an instance of a class that inherited
(directly or indirectly) from the specified class
otherwise False.
"""


def inherits_from(obj, a_class):
    """
        Return if obj is instance of class inherited
        from specified class
        Args:
            obj (any): the checked obj
            a_class (type): the class
        Return:
            True || False
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
