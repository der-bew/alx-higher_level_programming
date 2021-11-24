#!/usr/bin/python3
def weight_average(my_list=[]):
    '''a function that returns the weighted average of all integers
    tuple (<score>, <weight>)'''
    if my_list and len(my_list):
        num = 0
        dem = 0
        for tu in my_list:
            num += (tu[0] * tu[1])
            dem += tu[1]
        return (num / dem)
    return 0
