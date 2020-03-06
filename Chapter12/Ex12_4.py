
def make_word_dict(filename):
    d = dict()
    fin = open(filename)
    for line in fin:
        word = line.strip().lower()
        d[word] = None
    for letter in ['a','i','']:
        d[letter] = letter
    return d

"""
memo is a dictionary that maps from each word that is known
to be reducible to a list of its reducible children. It starts
with the empty string.
"""
memo = {}
memo[''] = ['']

def is_reducible(word, word_dict):
    if word in memo:
        return memo[word]

    res = []
    for child in children(word, word_dict):
        if is_reducible(child, word_dict):
            res.append(child)
    memo[word] = res
    return res

def children(word, word_dict):
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in word_dict:
            res.append(child)
    return res

def all_reducible(word_dict):
    res = []
    for word in word_dict:
        t = is_reducible(word, word_dict)
        if t != []:
            res.append(word)
    return res

def print_trail(word, word_dict):
    if len(word) == 0:
        return

    print(word, end=' ')
    t = is_reducible(word, word_dict)
    print_trail(t[0], word_dict)

def print_longest_words(word_dict):
    words = all_reducible(word_dict)
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)

    for _, word in t[0:5]:
        print_trail(word, word_dict)
        print('\n')

def main():
    word_dict = make_word_dict('words.txt')
    print_longest_words(word_dict)

if __name__ == '__main__':
    main()

