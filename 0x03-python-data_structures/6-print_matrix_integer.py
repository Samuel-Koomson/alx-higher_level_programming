#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for column in matrix:
        column_str = ''
        for element in column:
            column += '{:d} '.format(element)
        print(column_str[:-1])
