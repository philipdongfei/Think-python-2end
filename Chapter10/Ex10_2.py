def cumsum(t):
    c = []
    for i in range(len(t)):
        c.append(sum(t[:i+1]))
    return c


