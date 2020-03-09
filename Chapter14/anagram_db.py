import shelve
import sys

from anagram_sets import all_anagrams, signature

def store_anagrams(filename, anagram_map):
    """
    Stores the anagrams from a dictionary in a shelf.
    """
    shelf = shelve.open(filename, 'c')

    for word, word_list in anagram_map.items():
        print(word)
        shelf[word] = word_list
    shelf.close()

def read_anagrams(filename, word):
    """
    Looks up a word in a shelf and returns alist of its anagrams.
    """
    print('read anagrams word: ' , word)
    shelf = shelve.open(filename)
    sig = signature(word)
    try:
        return shelf[sig]
    except KeyError:
        return []

def main(script, command='make_db'):
    print('command= ', command)
    if command == 'make_db':
        anagram_map = all_anagrams('words.txt')
        store_anagrams('anagrams.db', anagram_map)
    else:
        # python anagram_db $word(value of command)
        print(read_anagrams('anagrams.db', command))

if __name__ == '__main__':
    main(*sys.argv)

