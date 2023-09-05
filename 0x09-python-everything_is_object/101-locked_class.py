#!/usr/bin/python3
""" LockedClass class module """


class LockedClass:
    """ Restrict creation of instance attribute except:
        for 'first_name'
    """
    __slots__ = ["first_name"]
