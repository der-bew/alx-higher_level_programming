#!/usr/bin/python3
def safe_print_integer_err(value):
    ''' prints an Integer '''
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        print("Exception: ", e)
        return False
