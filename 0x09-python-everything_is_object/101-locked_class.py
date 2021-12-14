#!/usr/bin/python3
""" Low memory cost """


class LockedClass:
    """ locked class created with lock atrr """

    __slots__ = ['first_name']

    def __init__(self, first_name=''):
        """ method with a first_name atrr """
        self.first_name = first_name
