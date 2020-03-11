import sys
import string
import random
class Markov:
    def __init__(self):
        self.suffix_map = {}
        self.prefix = ()
    def process_word(self, word, order=2):
        if len(self.prefix) < order:
            self.prefix += (word,)
            return
        try:
            self.suffix_map[self.prefix].append(word)
        except KeyError:
            #if there is no entry for this prefix, make one
            self.suffix_map[self.prefix] = [word]
        self.prefix = shift(self.prefix, word)

