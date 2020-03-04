
def has_no_e(word):
    if 'e' in word:
        return True
    return False

def percent_e(path):
    fin = open(path)
    count = 0
    total = 0
    for line in fin:
        word = line.strip()
        total += 1
        if has_no_e(word) == True:
            print(word)
            count += 1
    return count / total

def main():
    path = 'words.txt'
    print("words has e percent: %5.3f" %percent_e(path))
if __name__ == '__main__':
    main()
