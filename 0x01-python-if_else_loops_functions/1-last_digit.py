#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10 if number >= 0 else ((number * -1) % 10) * -1
if ld > 5:
    print("Last digit of {:d} is {:d} and is greater than {:d}"
          .format(number, ld, 5))
elif ld == 0:
    print("Last digit of {:d} is {:d} and is {:d}".format(number, ld, 0))
elif ld < 6 and ld != 0:
    print("Last digit of {:d} is {:d} and is less than {:d} and not {:d}"
          .format(number, ld, 6, 0))
