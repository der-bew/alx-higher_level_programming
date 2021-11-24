#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''A function that computes the square value of all integers of a matrix'''
    return list(map(lambda x: list(map(lambda y: y**2, x)), matrix))
