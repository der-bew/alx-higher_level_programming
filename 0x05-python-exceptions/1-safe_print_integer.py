#!/usr/bin/python3
def safe_print_integer(value):
    '''prints an integer with "{:d}".format()'''
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            return False
    except ValueError:
        print("Oops! value error happend")
