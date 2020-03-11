from OOTime import *
from MyPoint import Point
from print_attributes import print_attributes

start = Time()
start.hour = 9
start.minute = 45
start.second = 00
Time.print_time(start)
start.print_time()
end = start.increment(1337)
end.print_time()
print(end.is_after(start))
time = Time(9, 45)
print(time)
time.print_time()
start = Time(9, 45)
duration = Time(1, 35)
print(start + duration)
print(start + 1337)
print(1337 + start) # not define __radd__ : TypeError
p1 = Point()
p1.x = 5
p1.y = 6
p2 = Point()
p2.x = 7
p2.y = 8
p3 = p1 + p2
print((p3.x, p3.y))
p4 = p1 + (7, 8)
print((p4.x, p4.y))
t1 = Time(7, 43)
t2 = Time(7, 41)
t3 = Time(7, 37)
total = sum([t1,t2,t3])
print(total)
print(vars(total))
print_attributes(t1)





