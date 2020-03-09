from analyze_book1 import process_file
import random

def subtract(d1, d2):
    return set(d1) - set(d2)

def random_word(h):
    t = []
    for word, freq in h.items():
        t.extend([word] * freq)
    return random.choice(t)


def main():
    hist = process_file('emma.txt')
    words = process_file('words.txt')

    diff = subtract(hist, words)
    print("The words in the book that aren't in the word list are:")
    for word in diff:
        print(word, end=' ')
    print("Random word: ")
    print(random_word(hist))

if __name__ == '__main__':
    main()

