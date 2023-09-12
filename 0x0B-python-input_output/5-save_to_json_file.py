#!/usr/bin/python3
""" Save a Object to a File """
import json


def save_to_json_file(my_obj, filename):
    """
        Writes an Object to a text File,
        using a JSON string
        Args:
            my_obj (object): object to be saved
            filename (str): File name
    """
    with open(filename, 'w', encoding='utf-8') as myFile:
        json.dump(my_obj, myFile)
