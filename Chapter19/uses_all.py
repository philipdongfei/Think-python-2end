def uses_all(word, required):
    return all(letter in word for letter in required)
