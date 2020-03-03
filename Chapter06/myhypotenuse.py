import math

def hypotenuse(a, b):
    a2 = a**2
    b2 = b**2
    c = math.sqrt(a2+b2)
    return c

a = int(input('a='))
b = int(input('b='))
print('c = ', hypotenuse(a, b))
