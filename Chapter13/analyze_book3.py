import random
from bisect import bisect
from analyze_book1 import process_file

def random_word(hist):
    words = []
    freqs = []
    total_freq = 0

    for word, freq in hist.items():
        total_freq += freq
        words.append(word)
        freqs.append(total_freq)
    # choose a random value and find its location in the cumulative list
    x = random.randint(0, total_freq-1)
    index = bisect(freqs, x)
    #return (index, words[index])
    return words[index]

def main():
    hist = process_file('emma.txt')

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')

if __name__ == '__main__':
    main()

