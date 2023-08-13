#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    max_num = my_list[0]
    if length == 0:
        return "None"
    else:
        for item in my_list:
            if item > max_num:
                max_num = item
        return max_num
