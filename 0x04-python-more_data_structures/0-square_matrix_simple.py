#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) != 0:
        new_matrix = list(map((lambda x: [y ** 2 for y in x]), matrix))
    return new_matrix
