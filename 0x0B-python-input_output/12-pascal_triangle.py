#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """
        Returns a list of lists of integers representing
        the Pascal’s triangle of n
        Args:
            n (int): height of the pascal's triangle
    """
    if n <= 0:
        return []

    p_list = []
    for row in range(n):
        p_list.append([])
        for col in range(row):
            if len(p_list[row]) == 0:
                p_list[row].append(1)
                continue
            p_value = p_list[row - 1][col - 1] + p_list[row - 1][col]
            p_list[row].append(p_value)
        p_list[row].append(1)
    return p_list
