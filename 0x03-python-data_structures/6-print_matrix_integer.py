#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print()
    else:
        for row in matrix:
            for elem in row:
                if elem == row[len(row) - 1]:
                    print("{:d}".format(elem))
                else:
                    print("{:d}".format(elem), end=" ")
