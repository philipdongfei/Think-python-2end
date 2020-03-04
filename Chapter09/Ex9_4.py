
def uses_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True

def uses_letter_only(path, letters):
    fin = open(path)
    count = 0
    total = 0
    smallest = ''
    for line in fin:
        word = line.strip()
        total += 1
        if uses_only(word, letters):
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
    letters = input('uses only letters > ')
    print("words has e percent: %5.3f" %uses_letter_only(path, letters))
if __name__ == '__main__':
    main()
