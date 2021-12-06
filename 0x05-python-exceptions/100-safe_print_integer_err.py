#!/usr/bin/python3
def safe_print_integer_err(value):
    '''prints an Integer'''
    from sys import stderr
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        print("Exception: {}".format(e), file=stderr)
        return False
