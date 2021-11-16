#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
print_str5 = "Last digit of {:d} is {:d} and is greater than {:d}"
print_str6 = "Last digit of {:d} is {:d} and is less than {:d} and not {:d}"
if last_digit > 5:
    print(print_str5.format(number, last_digit, 5))
elif last_digit == 0:
    print("Last digit of {:d} is {:d} and is {:d}".format(number, last_digit, 0))
elif last_digit < 6 and last_digit != 0:
    print(print_str6.format(number, last_digit, 6, 0))
    
    
