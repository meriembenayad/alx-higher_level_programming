#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv)
    if arg <= 1:
        print("0")
    else:
        sum = 0
        for item in range(1, arg):
            sum += int(sys.argv[item])
        print("{:d}".format(sum))
