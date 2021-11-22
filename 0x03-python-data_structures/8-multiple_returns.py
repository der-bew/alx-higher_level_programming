def multiple_returns(sentence):
    '''
    INPUT:
      sentence: input sentence

    Function that returns a tuple with the length of a string and its
    first character
    '''
    if len(sentence) == 0:
        return None
    else:
        return len(sentence), sentence[0]
