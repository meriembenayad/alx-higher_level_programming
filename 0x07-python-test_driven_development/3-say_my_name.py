#!/usr/bin/python3
"""
    Method that print My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
        Prints my name
        Args:
            first_name (str): First name
            last_name (str): Last name
        Return:
            prints first name & last name
        Raises:
            TypeError: error message depends on the arg
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
