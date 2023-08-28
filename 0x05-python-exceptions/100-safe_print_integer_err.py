#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import exc_info as error, stderr
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        print("Exception: {}".format(error()[1]), file=stderr)
        return False
