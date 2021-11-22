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
        new_list = [False if x % 2 else True for x in my_list]
    return new_list
