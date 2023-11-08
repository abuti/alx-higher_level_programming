#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = set(my_list)
    u_sum = 0

    for i in s:
        u_sum += i

    return u_sum
