from Ex10_10 import in_bisect, make_word_list

def reverse_pair(word_list, word):
    rev_word = word[::-1]

    return in_bisect(word_list, rev_word)

def main():
    word_list = make_word_list()

    for word in word_list:
        if reverse_pair(word_list, word):
            print(word, word[::-1])

if __name__ == '__main__':
    main()

