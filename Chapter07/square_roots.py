epsilon = 0.0000001

def square_roots(x, a):
    while True:
        #print(x)
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return x
