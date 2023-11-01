#!/usr/bin/python3
prevFlag = True
for i in range(90, 64, -1):
    if prevFlag:
        c = i + 32
        prevFlag = False
    else:
        c = i
        prevFlag = True
    print("{}".format(chr(c)), end="")
