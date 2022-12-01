#!/usr/bin/python3
from sys import argv

total = 0
for i in range(1, len(argv)):
    total += int(argv[i])
print(total)
