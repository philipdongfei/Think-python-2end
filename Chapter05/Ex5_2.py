def check_fermat(a, b, c, n):
    if n > 2:
        if a**n + b**n == c**n:
            print('Holy smakes, Fermat was wrong!')
        else:
            print("No,that doesn't work.")
    else:
        print('n <= 2')

def main():
    a = int(input('Enter the numbe to a:'))
    b = int(input('Enter the numbe to b:'))
    c = int(input('Enter the numbe to c:'))
    n = int(input('Enter the numbe to n:'))
    check_fermat(a, b, c, n)
if __name__ == '__main__':
    main()


