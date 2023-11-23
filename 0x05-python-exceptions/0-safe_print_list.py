#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(0, x):
            print(my_list[i], end="")
        print()
        return x
    except IndexError:
        j = 0
        for i in my_list:
            j += 1
        print()
        return j
