#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''
    INPUT:
       matrix: input to be printed matrix

    Function that prints a matrix of integers
    '''
    for elm in matrix:
        print(" ".join("{:d}".format(i) for i in elm))
