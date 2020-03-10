import copy

class Time:
    """
    Represents the time of day.
    attributes: hour, minute, second.
    """
def print_time(t):
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))

def is_after(t1, t2):
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

def add_time(t1, t2):
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError('invalid Time object in add_time')
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)
    """
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
    return sum
    """

def increment(time, seconds):
    assert valid_time(time1)
    seconds1 = time_to_int(time)
    seconds1 += seconds
    return int_to_time(seconds1)
    """
    time.second += seconds

    if time.second >= 60:
        time.second -= 60
        time.minute += 1
    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1
    """
def pure_increment(time, seconds):
    t1 = Time()
    t1.second = time.second
    t1.minute = time.minute
    t1.hour = time.hour
    t1.second += seconds
    if t1.second >= 60:
        t1.second -= 60
        t1.minute += 1
    if t1.minute >= 60:
        t1.minute -= 60
        t1.hour += 1
    return t1

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def mul_time(t, mt):
    assert valid_time(t)
    seconds = time_to_int(t)
    seconds *= mt
    return int_to_time(seconds)

def time_per_mile(t1, dist):
    per = mul_time(t1, 1/dist)
    return per


