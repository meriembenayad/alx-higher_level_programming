#!/usr/bin/python3
""" Student to JSON with filter """
import json


class Student:
    """ Student class """

    def __init__(self, first_name, last_name, age):
        """
            Initialize the object
            Args:
                first_name (str): Student's First name
                last_name (str): Student's Last name
                age (int): Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Retrieves a dictionary representation of a Student instance
            Args:
                attrs (list): list of attributes
        """
        my_dict = {}
        if attrs is not None:
            for attr in attrs:
                try:
                    my_dict[attr] = self.__dict__[attr]
                except Exception:
                    pass
        else:
            return self.__dict__
        return my_dict
