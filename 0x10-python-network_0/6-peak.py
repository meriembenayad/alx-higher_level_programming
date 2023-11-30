#!/usr/bin/python3
""" Find a peak module """


def find_peak(list_of_integers):
    """ Finds a peak in a list of unsorted integers """
    if not list_of_integers:
        return None

    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]
    elif length == 2:
        return max(list_of_integers)

    for i in range(0, length - 1):
        if list_of_integers[i] >= list_of_integers[i - 1]\
                and list_of_integers[i] >= list_of_integers[i + 1]:
            return list_of_integers[i]

    return max(list_of_integers[0], list_of_integers[i - 1])
