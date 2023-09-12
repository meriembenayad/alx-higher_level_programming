#!/usr/bin/python3
""" Write to a File """


def write_file(filename="", text=""):
    """
        Write a string to a text file (UTF-8)
        and returns the number of characters written
        Args:
            filename (str): File name
            text (str): text to be added
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
