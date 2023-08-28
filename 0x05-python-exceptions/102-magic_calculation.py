#!/usr/bin/python3
import dis


def magic_calculation(a, b):
    try:
        result = a ** b - b
        return result
    except TypeError:
        return "Invalid input. a & b must be numbers"


dis.dis(magic_calculation)
