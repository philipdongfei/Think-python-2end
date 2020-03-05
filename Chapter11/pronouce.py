
def read_dictionary(filename='c06d.txt'):
    d = dict()
    fin = open(filename)
    for line in fin:
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d

def main():
    d = read_dictionary()
    for k, v in d.items():
        print(k, v)

if __name__ == '__main__':
    main()

