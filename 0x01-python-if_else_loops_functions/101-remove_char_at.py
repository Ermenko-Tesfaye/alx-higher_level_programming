#!/usr/bin/python3
def remove_char_at(str, n):
    strcp = ""
    if len(str) > n:
        for i in range(len(str)):
            if i != n:
                strcp += str[i]
        return strcp
    else:
        return str
