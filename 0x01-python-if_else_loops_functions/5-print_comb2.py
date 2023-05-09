#!/usr/bin/python3
for k in range(0, 100):
    if k != 100 - 1:
        print("{:02d}, ".format(k), end="")
    else:
        print("{:02d}".format(k))
