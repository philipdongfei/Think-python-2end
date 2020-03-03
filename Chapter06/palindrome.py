def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(w):
    if w == '':
        return True
    if first(w) != last(w):
        return False
    else:
        return is_palindrome(middle(w))
