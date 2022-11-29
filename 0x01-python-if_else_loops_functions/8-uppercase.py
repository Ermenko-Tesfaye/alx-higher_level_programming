#!/usr/bin/python3
def uppercase(str):
    value = 0
    for i in range(len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            value = ord(str[i]) - 32
        else:
            value = ord(str[i])
        print("{}".format(chr(value)), end="")
    print("")
