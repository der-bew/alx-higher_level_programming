#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ''' prints x elements of a list '''
    try:
        count = 0
        for i in my_list[0:x]:
            print("{}".format(i), end="")
            count += 1
        print("")
        return (count)
    except IndexError:
        print("Oops! Error happend \n")
