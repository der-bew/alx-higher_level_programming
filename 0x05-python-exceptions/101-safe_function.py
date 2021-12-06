#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        ret = fct(*args)
        return ret
    except Exception as e:
        print("Exception: {}".format(e), file=stderr)
        return None
