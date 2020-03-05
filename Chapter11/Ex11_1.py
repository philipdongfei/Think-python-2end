def create_dict(path):
    fin = open(path)
    d = dict()
    for line in fin:
        word = line.strip()
        d[word] = 1
    return d

def main():
    word = input("Enter one word: ")
    word_dict = create_dict('words.txt')
    print(word in word_dict)

if __name__ == '__main__':
    main()


