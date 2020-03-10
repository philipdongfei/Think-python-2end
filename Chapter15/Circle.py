from Point import *
from Rectangle import *
from print_point import *
import math
import copy

class Circle:
    """Represents a circle
    attributes: center, radius
    """

def distance_between_point(p1, p2):
    return math.sqrt(abs(p1.x-p2.x)**2 + abs(p1.y-p2.y)**2)

def point_in_circle(p, c):
    dist = distance_between_point(p, c.center)
    if dist < c.radius:
        return True
    return False

def rect_in_circle(rect, c):
    p = copy.copy(rect.corner)
    print_point(p)
    if not point_in_circle(p, c):
        return False

    p.x += rect.width
    print_point(p)
    if not point_in_circle(p, c):
        return False

    p.y -= rect.height
    print_point(p)
    if not point_in_circle(p, c):
        return False

    p.x -= rect.width
    print_point(p)
    if not point_in_circle(p, c):
        return False

    return True

def rect_circle_overlap(rect, c):
    p = copy.copy(rect.corner)
    print_point(p)
    if point_in_circle(p, c):
        return True

    p.x += rect.width
    print_point(p)
    if point_in_circle(p, c):
        return True
    p.y -= rect.height
    print_point(p)
    if point_in_circle(p, c):
        return True
    p.x -= rect.width
    print_point(p)
    if point_in_circle(p, c):
        return True

    return False

def main():
    c = Circle()
    c.center = Point()
    c.center.x = 150.0
    c.center.y = 100.0
    c.radius = 75
    p = Point()
    p.x = float(input('enter p.x: '))
    p.y = float(input('enter p.y: '))

    print_point(p)
    box = Rectangle()
    box.width = 100.0
    box.heigth = 200.0
    box.corner = Point()
    box.corner.x = float(input('enter box corner x: '))
    box.corner.y = float(input('enter box corner y: '))
    print('box.corner: ')
    print_point(box.corner)
    print()

    print(point_in_circle(p, c))
    print(rect_in_circle(box, c))
    print(rect_circle_overlap(box, c))


if __name__ == '__main__':
    main()


