#!/usr/bin/python3
""" Search and Update """


def append_after(filename="", search_string="", new_string=""):
    """
        Inserts a line of text to a file,
        after each line containing a specific string
        Args:
            filename (str): File name
            search_string (str): string to be search for
            new_string (str): string to be replaced by
    """
    with open(filename, mode='r', encoding='utf-8') as myFile:
        lines = []
        while True:
            line = myFile.readline()
            if line == "":
                break
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
    with open(filename, mode='w', encoding='utf-8') as myFile:
        myFile.writelines(lines)
