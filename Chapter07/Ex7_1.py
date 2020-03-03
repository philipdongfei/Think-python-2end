from square_roots import *
import math

def mysqrt(a):
    return square_roots(5, a)

def test_square_root():
    space = ' '
    print('a',space*4,'mysqrt(a)',space*6,'math.sqrt(a)',space*3,'diff')
    print('-',space*4,'-'*9,space*6,'-'*12,space*3,'-'*4)
    for a in range(1, 10, 1):
        print(a, end = ' '*4)
        x = mysqrt(a)
        print("%14.10f" % x, end=' ')
        y = math.sqrt(a)
        print("%14.10f" % y, end=' ')
        #print(y , end=' ' * (15-len(str(y))))
        z = x - y
        #print(z)
        print("%14.10f" % z)



def main():
    test_square_root()

if __name__ == '__main__':
    main()


