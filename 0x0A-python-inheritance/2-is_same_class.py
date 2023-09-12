#!/usr/bin/python3
"""
Write a function that returns:
True if the object is exactly an instance of the specified class
otherwise False
"""


def is_same_class(obj, a_class):
    """
        Check if object is an instance of class
        Args:
            obj (any): object to ckeck
            a_class (type): the class
        Return:
            True: if obj is an instance of the specified class
            False: Otherwise
    """
    if type(obj) == a_class:
        return True
    else:
        return False
