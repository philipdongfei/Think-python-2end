def is_triangle(a, b, c):
    if (a + b) < c or (a + c) < b or (b + c) < a:
        print("No")
    else:
        print("Yes")

def main():
    a = int(input('Enter the a:'))
    b = int(input('Enter the b:'))
    c = int(input('Enter the c:'))
    is_triangle(a, b, c)

if __name__ == '__main__':
    main()

