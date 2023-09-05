#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

matrix_str = [
    [1, "2", 3],
    [4, "5", 6]
]
try:
    print(matrix_divided(matrix_str, 3))
except Exception as e:
    print(e)


matrix_not = [
    [1, 2, 3],
    [4, 6]
]
try:
    print(matrix_divided(matrix_not, 3))
except Exception as e:
    print(e)

matrix_div0 = [
    [1, 2, 3],
    [4, 6, 7]
]
try:
    print(matrix_divided(matrix_div0, 0))
except Exception as e:
    print(e)
