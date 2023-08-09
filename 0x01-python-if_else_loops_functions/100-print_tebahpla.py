#!/usr/bin/python3
for letter in range(ord('z'), ord('a') - 1, -1):
    if letter % 2 != 0:
        letter -= 32
    print("{}".format(chr(letter)), end="")
