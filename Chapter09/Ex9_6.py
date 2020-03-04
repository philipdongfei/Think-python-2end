def is_abecedarian(word):
    word = word.lower()
    preletter = word[0]
    for letter in word[1:]:
        if letter < preletter:
            return False
        else:
            preletter = letter
    return True

def word_is_abecedarian(path):
    fin = open(path)
    count = 0
    total = 0
    smallest = ''
    for line in fin:
        word = line.strip()
        total += 1
        if is_abecedarian(word):
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
    #letters = input('uses all letters > ')
    print("words is abecedarian: %9.7f" %word_is_abecedarian(path))
if __name__ == '__main__':
    main()
