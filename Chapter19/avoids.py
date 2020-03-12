def avoids(word, forbidden):
    '''
    word: type is string.
    forbidden: type is string.
    '''
    return not any(letter in forbidden for letter in word)
    #return len(set(word) & set(forbidden)) == 0

