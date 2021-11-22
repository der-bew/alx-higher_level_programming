#!/usr/bin/python3
def max_integer(my_list=[]):
    '''
    INPUT:
       my_list: input list
    RETURN:
       None or max number

    Function that finds the biggest integer of a list
    '''
    if my_list:
        max = 0
        for elm in my_list:
            if elm > max:
                max = elm
        return max
    return None
