import string

def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

def total_words(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)

def most_common(hist):
    t = []
    for key, value in hist.items():
        t.append((value, key))
    t.sort(reverse=True)
    return t

def print_most_common(hist, num=10):
    t = most_common(hist)
    print('The most common words are: ')
    for freq, word in t[:num]:
        print(word, freq, sep='\t')
def subtract(d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

"""

hist = process_file('emma.txt')
print('Total number of words: ', total_words(hist))
print('Number of different words: ', different_words(hist))
print_most_common(hist, 20)
words = process_file('words.txt')
diff = subtract(hist, words)
print("Words in the book that aren't in the word list: ")
for word in diff:
    print(word, end=' ')
    print()

"""




