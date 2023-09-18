#!/usr/bin/python3
""" Calculator Method """


def add(x, y):
    """ Addition """
    return x + y


def sub(x, y):
    """ Substraction """
    return x - y


def mul(x, y):
    """ Multiplication """
    return x * y


def div(x, y):
    """ Division """
    if y == 0:
        raise ValueError("Can(t divide by zero!)")
    return x / y


def mod(x, y):
    """ Modulo """
    if y == 0:
        raise ValueError("Can't divide by zero!")
    return x % y
