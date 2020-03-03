import math
from mydistance import distance

def area(r):
    return math.pi*r**2

def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result

print('area = ', circle_area(1,1, 4, 4))



