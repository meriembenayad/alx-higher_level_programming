#!/usr/bin/python3
def remove_char_at(str, n):
    ch = ""
    for letter in range(len(str)):
        if letter != n:
            ch += str[letter]
    return (ch)
