from rotate import rotate_word

def make_word_dict():
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = None

    return d

def rotate_pairs(word, word_dict):
    for i in range(1, 14):
        rotated = rotate_word(word, i)
        if rotated in word_dict:
            print(word, i, rotated)

def main():
    word_dict = make_word_dict()
    for word in word_dict:
        rotate_pairs(word, word_dict)

if __name__ == '__main__':
    main()

