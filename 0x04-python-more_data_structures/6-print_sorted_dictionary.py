#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key = sorted(dict(a_dictionary).keys())
    for item in key:
        print("{}: {}".format(item, a_dictionary[item]))
