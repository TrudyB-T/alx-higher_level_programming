#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        new_row = []
        for elmnt in row:
            new_elmnt = elmnt * elmnt
            new_row.append(new_elmnt)
            print("{:d}".format(elmnt), end=' ' if elmnt != row[-1] else '')
        new_matrix.append(new_row)
        print()

    return new_matrix
