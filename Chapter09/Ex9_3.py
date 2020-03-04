
def avoids(word, letters):
    for letter in letters:
        if letter in word:
            return False
    return True

def forbidden_letter(path, letters):
    fin = open(path)
    count = 0
    total = 0
    smallest = ''
    for line in fin:
        word = line.strip()
        total += 1
        if avoids(word, letters):
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
    letters = input('forbidden letters > ')
    print("words has e percent: %5.3f" %forbidden_letter(path, letters))
if __name__ == '__main__':
    main()
