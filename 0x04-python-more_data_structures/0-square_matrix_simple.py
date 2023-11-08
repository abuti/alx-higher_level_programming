#!/usr/bin/python3
def square(x):
    return (x ** 2)


def square_matrix_simple(matrix=[]):
    new_mat = []
    for i in matrix:
        new_ele = list(map(square, i))
        new_mat.append(new_ele)
    return new_mat
