#!/usr/bin/python3
def pow(a, b):
    p = 1
    if b == 0:
        return 1
    if b < 0:
        b = -1 * b
        a = float(a)
        a = 1 / a
    for i in range(0, b):
        p = p * a
    return p
