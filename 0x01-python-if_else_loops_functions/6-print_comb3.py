#!/usr/bin/python3
for m in range(0, 10):
    for n in range(1, 10):
        if m >= n:
            continue
        elif m == 8 and n == 9:
            print("{}{}".format(m, n))
        else:
            print("{}{}, ".format(m, n), end="")
