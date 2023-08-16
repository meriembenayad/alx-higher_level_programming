#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda ro: list(map(lambda co: co ** 2, ro)), matrix)))
