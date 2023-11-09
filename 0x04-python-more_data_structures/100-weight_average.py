#!/usr/bin/python3
def add_list_ele(my_list):
    s = 0
    for i in my_list:
        s += i
    return s


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    list_1 = []
    list_2 = []
    for i in my_list:
        list_1.append(i[0] * i[1])
        list_2.append(i[1])
    return add_list_ele(list_1) / add_list_ele(list_2)
