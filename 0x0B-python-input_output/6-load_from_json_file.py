#!/usr/bin/python3
""" Create object from a JSON file """
import json


def load_from_json_file(filename):
    """
        Creates an object from JSON file
        Args:
            filename (str): File name
    """
    with open(filename, mode='r', encoding='utf-8') as myFile:
        return json.load(myFile)
