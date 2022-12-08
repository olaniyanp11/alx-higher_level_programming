#!/usr/bin/pytho n3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if row != None:
            for column in row:
                print("{}".format(column), end=" ")
            print("")
        else:
            print("")
