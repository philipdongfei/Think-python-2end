def uses_all(word, letters):
    for letter in letters:
        if letter not in word:
            return False
    return True

def word_include_letters(path, letters):
    fin = open(path)
    count = 0
    total = 0
    smallest = ''
    for line in fin:
        word = line.strip()
        total += 1
        if uses_all(word, letters):
            print(word)
            length = len(smallest)
            if length == 0:
                smallest = word
            elif length > len(word):
                smallest = word
            count += 1
    print('smallest word:', smallest)
    return count / total

def main():
    path = 'words.txt'
    letters = input('uses all letters > ')
    print("words include letters: %9.7f" %word_include_letters(path, letters))
if __name__ == '__main__':
    main()
