#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    '''
    INPUT:
       my_list: input list
       idx: the index number
       element: the element to be inserted at the given idx

    Replaces an element of a list at a specific position
    '''
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
