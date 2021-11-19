#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    ''' INPUT:
           my_list: input list
    Prints all integers of a list, in reverse order
    '''
    my_list.reverse()
    for i in my_list:
        print("{}".format(i))
