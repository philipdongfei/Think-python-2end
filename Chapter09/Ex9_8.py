def has_palindrome(i, start, length):
    s = str(i)[start:start+length]
    return s[::-1] == s

def check(i):
    return (has_palindrome(i, 2, 4) and
            has_palindrome(i+1, 1, 5) and
            has_palindrome(i+2, 1, 4) and
            has_palindrome(i+3, 0, 6))

def check_all():
    i = 1000000
    while i <= 9999996:
        if check(i):
            print(i)
        i = i + 1

def main():
    check_all()

if __name__ == '__main__':
    main()

