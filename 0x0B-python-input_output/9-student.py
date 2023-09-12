#!/usr/bin/python3
""" Student to JSON """
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

    def to_json(self):
        """
            Retreives a dictionary representation of a Student instance
        """
        return self.__dict__
