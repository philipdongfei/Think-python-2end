def is_sorted(t):
    prew = t[0]
    for w in t[1:]:
        if prew <= w:
            prew = w
        else:
            return False
    return True



