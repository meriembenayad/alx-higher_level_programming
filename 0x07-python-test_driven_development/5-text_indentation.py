#!/usr/bin/python3
"""
    Module thats prints a text with 2 new lines,
    after each of these characters: . , ? and :
"""


def text_indentation(text):
    """
        Prints a text with 2 new lines after
        each specified characters: . , ? and :
        Args:
            text (str): text
        Return:
            new text modified
        Raises:
            TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    charcters = ".?:"
    new_text = ""
    line = ""

    for char in text:
        line += char
        if char in charcters:
            new_text += line.strip() + "\n\n"
            line = ""

    if line:
        new_text += line.strip()

    print(new_text, end="")
