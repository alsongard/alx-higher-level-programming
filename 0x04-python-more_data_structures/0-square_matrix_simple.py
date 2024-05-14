#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    super_matrix = []
    for item in matrix:
        new_matrix = []
        for number in item:
            new_matrix.append(number ** 2)
        super_matrix.append(new_matrix)
    return super_matrix
