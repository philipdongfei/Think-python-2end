def is_anagram(w1, w2):
    '''
    Two words are anagrams if you can rearrange the letters from one to
    spell the other.
    '''
    #return sorted(w1) == sorted(w2)
    return Counter(w1) == Counter(w2)


