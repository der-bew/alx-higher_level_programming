#!/usr/bin/python3
def element_at(my_list, idx):
    """ INPUT:
          my_list: input list
          idx: Index number of the retrieve element
        RETURN:
           None or element
    Retrieves an element from a list
    """

    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
