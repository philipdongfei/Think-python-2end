
def most_frequest(s):
    hist = make_histogram(s)
    t = []
    for x, freq in hist.items():
        t.append((freq, x))

    t.sort(reverse=True)

    res = []
    for freq, x in t:
        res.append(x)

    return res

def make_histogram(s):
    hist = {}
    #t = s.split(" ")
    t = s
    for x in t:
        hist[x] = hist.get(x, 0) + 1
    return hist

def read_file(filename):
    return open(filename).read()

def main():
    string = read_file('emma.txt')
    letter_seq = most_frequest(string)
    for x in letter_seq:
        print(x)

if __name__ == '__main__':
    main()

