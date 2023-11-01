#!/usr/bin/python3
def pow(a, b):
    p = 1
    reciprocalFlag = False
    if b == 0:
        return 1
    elif b < 0:
        reciprocalFlag = True
        b = -1 * b
    for i in range(0, b):
        p = p * a
    if reciprocalFlag:
        p = float(1 / p)
    return p
