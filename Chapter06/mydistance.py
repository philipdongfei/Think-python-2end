import math

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

def main():
    x1 = int(input('x1='))
    y1 = int(input('y1='))
    x2 = int(input('x2='))
    y2 = int(input('y2='))
    d = distance(x1,y1,x2,y2)
    print("distance = ",d)

if __name__ == '__main__':
    main()
