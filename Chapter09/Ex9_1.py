def count20er(path):
    fin = open(path)
    count = 0
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)
            count += 1
    return count

def main():
    path = 'words.txt'
    print('words more than 20 characters: ', count20er(path))

if __name__ == '__main__':
    main()


