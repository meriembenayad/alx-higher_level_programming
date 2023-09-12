#!/usr/bin/python3
""" Read File """


def read_file(filename=""):
    """
        Read text file in utf-8
        print it in stdout
        Args:
            filename (str): File name
    """
    with open("my_file_0.txt", mode="r", encoding="utf-8") as myFile:
        print(myFile.read())
