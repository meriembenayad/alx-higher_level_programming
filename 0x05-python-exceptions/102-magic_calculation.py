#!/usr/bin/python3
import dis


def magic_calculation(a, b):
    result = 0
    for ele in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += a ** b / ele
        except:
            result += b + a
            break
    return result


dis.dis(magic_calculation)
