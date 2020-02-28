import turtle
import math


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t, length, n):
    degrees = 360 / n
    radius = degrees / 180.0 * math.pi
    for i in range(n):
        t.fd(length)
        t.lt(degrees)

def circle(t, r):
    c = 2.0 * math.pi * r
    n = int(c / 3) + 1
    len = c / n
    polygon(t, len, n)
    '''

    for n in range (44, 50, 2):
        len = c / n
        polygon(t, len, n)
    '''

def arc(t, r, angle):
    arc_c = angle / 180.0 * math.pi * r
    c = 2.0 * math.pi * r
    arc_degrees = angle
    for n in range(6, 20, 2):
        t.pd()
        arc_degrees = angle
        len = c / float(n)
        degrees = 360 / n
        for i in range(n):
            t.fd(len)

            if arc_degrees > 0:
                if (arc_degrees - degrees) >= 0:
                    arc_degrees -= degrees
                else:
                    #degrees = arc_degrees
                    arc_degrees = 0
            else:
                t.pu()
            t.lt(degrees)

bob = turtle.Turtle()
'''

bob.rt(90)
bob.fd(100)
bob.lt(90)
arc(bob, 100, 220)
'''
circle(bob, 100)
#square(bob, 50)
#polygon(bob, 30, 6)
turtle.mainloop()


'''

print(bob)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
for i in range(4):
    bob.fd(100)
    bob.lt(90)
turtle.mainloop()
'''
