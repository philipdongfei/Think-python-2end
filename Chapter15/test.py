from Point import *
from Rectangle import *
from grow_rectangle import *
from find_center import *
from print_point import *
from move_rectangle import *

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0
center = find_center(box)
print_point(center)
box.width = box.width + 50
box.height = box.height + 100
print((box.width, box.height))
grow_rectangle(box, 50, 100)
print((box.width, box.height))
box2 = move_rectangle(box, 5, 5)
print_point(box.corner)
print_point(box2.corner)
