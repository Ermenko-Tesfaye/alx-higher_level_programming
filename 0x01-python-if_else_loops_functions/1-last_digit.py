#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
rem = 0
myStr = "and is less than 6 and not 0"
if number < 0:
    rem = (number * -1) % 10
    rem *= -1
else:
    rem = number % 10
if rem > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, rem))
elif rem == 0:
    print("Last digit of {} is {} and is 0".format(number, rem))
else:
    print("Last digit of {} is {} {}".format(number, rem, myStr))
