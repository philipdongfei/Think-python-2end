import string

def make_word_list(filename):
    word_list = []
    fin = open(filename)
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list

def txt2word(filename):
    fin = open(filename)
    d = dict()
    strippables = string.punctuation + string.whitespace
    for line in fin:
        line = line.replace('-',' ')
        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
            d[word] = d.get(word,0)+1
    return d

def norealwords(filename, word_dict):
    fin = open(filename)
    d = dict()
    strippables = string.punctuation + string.whitespace
    for line in fin:
        line = line.replace('-',' ')
        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
            if word not in word_dict:
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
    word_dict = make_word_list('words.txt')
    books = ['emma.txt', 'songs.txt', 'PrideAndPrejudice.txt']
    for book in books:
        print(book, ': ')
        no_in_real_dict = dict()
        no_in_real_dict = norealwords(book, word_dict)
        #for key in word_dict:
        #    print(key, word_dict[key])
        print("Total words(no in real words): %d" % total_words(no_in_real_dict))
        print("Different words(no in real words): %d" % different_words(no_in_real_dict))
        print_most_common(no_in_real_dict)
        print()

if __name__ == '__main__':
    main()



