#!/usr/bin/python3
""" To JSON string """
import json


def to_json_string(my_obj):
    """
        Returns the JSON representation of an object (string)
        Args:
            my_obj (str): the object
    """
    return json.dumps(my_obj)
