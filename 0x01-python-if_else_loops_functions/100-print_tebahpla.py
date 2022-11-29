#!/usr/bin/python3
num = 122
for i in range(26):
    if num % 2 == 0:
        print("{}".format(chr(num)), end="")
    else:
        print("{}".format(chr(num - 32)), end="")
    num = num - 1
