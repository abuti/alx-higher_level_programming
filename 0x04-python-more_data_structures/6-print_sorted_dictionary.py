#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    _list = sorted(list(a_dictionary))
    for i in _list:
        print("{:s}: {}".format(i, a_dictionary[i]))
