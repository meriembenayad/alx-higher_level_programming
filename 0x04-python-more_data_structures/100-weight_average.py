#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total = 0
    weight = 0
    for x, y in my_list:
        total += x * y
        weight += y
    avg = total / weight
    return avg
