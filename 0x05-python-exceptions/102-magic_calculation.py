#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for ele in range(1, 3):
        try:
            if ele > a:
                raise Exception('Too far')
            else:
                result += a ** b / ele
        except Exception:
            result = b + a
            break
    return result
