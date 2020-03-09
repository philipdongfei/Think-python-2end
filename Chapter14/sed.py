
def sed(pattern, replace, source, dest):
    fin = open(source, 'r')
    fout = open(dest, 'w')

    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)

    fin.close()
    fout.close()

def main():
    pattern = 'pattern'
    replace = 'replace'
    source = 'sed_tester.txt'
    dest = source + '.replaced'
    sed(pattern, replace, source, dest)

if __name__ == '__main__':
    main()

