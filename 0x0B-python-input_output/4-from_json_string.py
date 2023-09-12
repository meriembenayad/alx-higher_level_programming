#!/usr/bin/python3
""" From JSON string to Object """
import json


def from_json_string(my_str):
    """
        Returns an object (Python Data Structure)
        represented by a JSON string
        Args:
            my_str (str): string
    """
    return json.loads(my_str)
