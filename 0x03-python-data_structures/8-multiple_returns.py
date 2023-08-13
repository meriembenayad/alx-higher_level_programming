#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0]
    if length == 0:
        return 0, None
    else:
        return length, first_char
