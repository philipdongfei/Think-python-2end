from MyTime import *

start = Time()
start.hour = 9
start.minute = 45
start.second = 0
duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0
done = add_time(start, duration)
print_time(done)
t1 = pure_increment(done, 20)
print_time(t1)

race_time = Time()
race_time.hour = 1.0
race_time.minute = 34.0
race_time.second = 5.0
print_time(race_time)
distance = 13.1 # miles
print('dist:', distance)
pace = time_per_mile(race_time, distance)
print_time(pace)


