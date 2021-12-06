#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ''' prints x elements of a list '''
    try:
        for i in my_list[0:x]:
            print("{}".format(i), end="")
        print("")
        return (i)
    except IndexError as e:
        return (e)
