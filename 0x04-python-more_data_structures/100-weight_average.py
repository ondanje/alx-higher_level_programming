#!/usr/bin/python3

def weight_average(my_list=[]):

    if not my_list:
        return 0

    numerator = 0
    denominator = 0

    for val in my_list:
        numerator += val[0] * val[1]
        denominator += val[1]

    return (numerator / denominator)
