#!/usr/bin/python3
""" class MyInt that inherits from int """


class MyInt(int):
    """ a rabel int """

    def __eq__(self, value):
        """ equal revert to not equal """
        return super().__ne__(value)

    def __ne__(self, value):
        """ not equal revert to equal """
        return super().__eq__(value)
