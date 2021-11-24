#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    '''INPUT:
         a_dictionary: Input dictionary
         key: argument will be always a string
         value: argument will be any type
       RETURN: a dictionary

    A function that replaces or adds key/value in a dictionary
    '''
    a_dictionary[key] = value
    return a_dictionary
