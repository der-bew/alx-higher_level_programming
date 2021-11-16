#!/usr/bin/python3
def fizzbuzz():
    """ Function that prints the numbers from 1 to 100 separated by a space.
     For multiples of three print Fizz instead of the number and for multiples
     of five print Buzz.
     For numbers which are multiples of both three and five print FizzBuzz."""

    for x in range(1, 101):
        if x % 5 == 0 and x % 3 == 0:
            print("FizzBuzz", end=" ")
        elif x % 3 == 0:
            print("Fizz", end=" ")
        elif x % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(x), end=" ")
