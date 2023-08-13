#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    max_num = my_list[0]
    for item in my_list:
        if max_num < item:
            max_num = item
    return max_num
