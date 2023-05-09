#!/usr/bin/python3
def remove_char_at(str, n):
    # result to store copy of string
    result = ''
    for i in range(len(str)):
        if i != n:
            result += str[i]

    return result
