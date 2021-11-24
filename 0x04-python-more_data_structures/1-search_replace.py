#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''
    INPUT:
      my_list: is the initial list
      search: is the element to replace in the list
      replace: is the new element
    RETURN: new list

    A function that replaces all occurrences of an element by another 
    in a new list
    '''
    return list(map(lambda x: x if x != search else replace, my_list))
