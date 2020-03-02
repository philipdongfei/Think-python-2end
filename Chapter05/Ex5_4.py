def recurse(n, s):
    """
    if n is less than 0,
    the function is infinite recursion.
    """
    if n==0:
        print(s)
    else:
        recurse(n-1, n+s)

def main():
    n = int(input('Enter the n: '))
    s = int(input('Enter the s: '))
    recurse(n, s)
if __name__ == '__main__':
    main()

