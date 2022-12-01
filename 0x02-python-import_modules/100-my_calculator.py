#!/usr/bin/python3
from calculator_1 import *
from sys import argv

if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
num1, num2 = int(argv[1]), int(argv[3])
if argv[2] == '+':
    print("{} + {} = {}".format(num1, num2, add(num1, num2)))
    exit(0)
elif argv[2] == '-':
    print("{} - {} = {}".format(num1, num2, sub(num1, num2)))
    exit(0)
elif argv[2] == '*':
    print("{} * {} = {}".format(num1, num2, mul(num1, num2)))
    exit(0)
elif argv[2] == '/':
    print("{} / {} = {}".format(num1, num2, div(num1, num2)))
    exit(0)
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
