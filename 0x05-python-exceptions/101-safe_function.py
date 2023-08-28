#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        new = fct(*args)
    except Exception as exc:
        sys.stderr.write("Exception: {}\n".format(exc))
        '''
        print("Exception: {}".format(e), file=sys.stderr)
        '''
        return None
    return new
