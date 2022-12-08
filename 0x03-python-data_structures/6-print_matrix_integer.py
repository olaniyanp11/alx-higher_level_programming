#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if row != None:
            for column in row:
                print("{:d}".format(column), end=" ")
            print("")
        else:
            print("")
