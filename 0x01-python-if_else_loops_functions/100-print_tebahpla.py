#!/usr/bin/python3
prevFlag = True
for i in range(90, 65, -1):
    if prevFlag:
        c = i + 32
        prevFlag = False
    else:
        c = i
        prevFlag = True
    print(f"{chr(c)}", end="")
