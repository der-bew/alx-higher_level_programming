#!/usr/bin/python3
def element_at(my_list, idx):
    """ Retrieves an element from a list
    If idx is negative, the function should return None
    If idx is out of range (> of number of element in my_list),
    the function should return None
    You are not allowed to import any module
    """

    if idx < 0 and idx >= len(my_list):
        return None
    else:
        return my_list[idx]
