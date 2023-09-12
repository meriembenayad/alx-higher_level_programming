#!/usr/bin/python3
""" Append to a file """


def append_write(filename="", text=""):
    """
        Appends a string at the end of a text file (UTF-8)
        and returns the number of characters added
        Args:
            filename (str): File Name
            text (str): text to be added
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return myFile.write(text)
