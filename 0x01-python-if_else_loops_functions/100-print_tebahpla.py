#!/usr/bin/python3
for letter in range(ord('z'), ord('a') -1, -1):
    if letter % 2 == 0:
        print(chr(letter), end="")
    else:
        print(chr(letter - ord('a') + ord('A')), end="")
