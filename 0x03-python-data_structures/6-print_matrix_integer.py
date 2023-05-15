#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        s = 1
        for element in row:
            if s == len(row):
                print("{:d}".format(element), end="")
            else:
                print("{:d}".format(element), end=" ")
            s = s + 1
        print()
