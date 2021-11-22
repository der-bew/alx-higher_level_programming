def multiple_returns(sentence):
    '''
    INPUT:
      sentence: input sentence

    Function that returns a tuple with the length of a string and its
    first character
    '''
    my_tuple = tuple(sentence)
    if len(my_tuple) == 0:
        return (len(my_tuple), None)
    else:
        return (len(my_tuple), my_tuple[0])
