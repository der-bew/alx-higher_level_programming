#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    '''
    INPUT:
      my_list: input list
    RETURN:
      new list with True or false

    Function that finds all multiples of 2 in a list
    '''
    if my_list:
        new_list = [True if x % 2 == 0 else False for x in my_list]
    return new_list
