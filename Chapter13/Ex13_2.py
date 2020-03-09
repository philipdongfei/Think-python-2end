import string

def txt2word(filepath):
    fin = open(filepath)
    d = dict()
    strippables = string.punctuation + string.whitespace
    for line in fin:
        line = line.replace('-',' ')
        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
            d[word] = d.get(word,0)+1
    return d
def most_common(wd):
    t = []
    for key, value in wd.items():
        t.append((value, key))

    t.sort()
    t.reverse()
    return t
def print_most_common(wd, num=10):
    t = most_common(wd)
    print('The most common words are: ')
    for freq, word in t[:num]:
        print(word, '\t', freq)


def total_words(word_dict):
    return sum(word_dict.values())

def different_words(word_dict):
    return len(word_dict)

def main():
    books = ['emma.txt', 'songs.txt', 'PrideAndPrejudice.txt']
    for book in books:
        print(book, ': ')
        word_dict = txt2word(book)
        #for key in word_dict:
        #    print(key, word_dict[key])
        print("Total words: %d" % total_words(word_dict))
        print("Different words: %d" % different_words(word_dict))
        print_most_common(word_dict)
        print()

if __name__ == '__main__':
    main()



