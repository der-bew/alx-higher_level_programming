#!/usr/bin/python3
def safe_print_integer_err(value):
    '''prints an Integer'''
    from sys import stderr
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        stderr.write("Exception: {}".format(e))
        return False
