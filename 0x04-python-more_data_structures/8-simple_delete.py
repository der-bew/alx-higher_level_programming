#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    '''INPUT:
         a_dictionary: Input dictionary
         key: argument will be always a string

       RETURN: a dictionary
    A function that deletes a key in a dictionary
    '''
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
