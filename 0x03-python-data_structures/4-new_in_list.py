#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''
    INPUT:
        my_list: input list
        idx: the index  number which the element replaced
        element: the new element to be added

    Function that replaces an element in a list at a specific position
    without modifying the original list
    '''
    new_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_list[idx] = element
        return new_list
