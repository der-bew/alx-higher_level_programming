#!/usr/bin/python3
def no_c(my_string):
    '''
    INPUT:
       my_string: input string

    Function that removes all characters c and C from a string
    '''
    new_str = ""
    for x in my_string:
        if x != 'c' and x != 'C':
            new_str += x
    return new_str
