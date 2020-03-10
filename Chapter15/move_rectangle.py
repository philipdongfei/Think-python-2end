from Rectangle import *
from Point import *
import copy

def move_rectangle(rect, dx, dy):
    rect2 = copy.deepcopy(rect)
    rect2.corner.x += dx
    rect2.corner.y += dy
    return rect2

