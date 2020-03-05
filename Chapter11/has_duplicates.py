def has_duplicates(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False
def has_duplicates2(t):
    return len(set(t)) < len(t)

def main():
    t = [1,2,3]
    print(has_duplicates(t))
    t.append(1)
    print(has_duplicates(t))
    t = [1,2,3]
    print(has_duplicates2(t))
    t.append(1)
    print(has_duplicates2(t))

if __name__ == '__main__':
    main()

