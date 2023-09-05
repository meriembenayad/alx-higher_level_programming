#!/usr/bin/python3
""" nqueens define """
import sys
def nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def place_queen(board, row, col, N):
        """ Check if there is a queen in the same column """
        for i in range(row):
            if board[i][col] == 1:
                return False

        """ Check if there is a queen upper left diagonal """
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        """ Check if there is a queen upper right diagonal """
        for i, j in zip(range(row, -1, -1), range(col, N)):
            if board[i][j] == 1:
                return False

        return True

    def solve_nqueen(board, row):
        