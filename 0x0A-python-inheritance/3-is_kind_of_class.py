#!/usr/bin/python3
"""
function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
        Return True or False depends of instance of the objectù
        Args:
            obj (any): the object that checked
            a_class (type): the class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
