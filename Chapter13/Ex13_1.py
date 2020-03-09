import string

def txt2word(filepath):
    fin = open(filepath)
    d = dict()
    strippables = string.punctuation + string.whitespace
    for line in fin:
        line = line.replace('-',' ')
        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
            d[word] = d.get(word,0)+1
    return d

word_dict = txt2word('emma.txt')
for key in word_dict:
    print(key, word_dict[key])

