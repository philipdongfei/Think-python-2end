def is_power(a, b):
    if a == b:
        return True
    elif a < b:
        return False
    if a % b != 0:
        return False
    return is_power(a/b, b)
