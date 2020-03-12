class Point:
    """Represents a point in 2-D space."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)
    def __add__(self, other):
        p = Point()
        if isinstance(other, tuple):
            p.x, p.y = self.x+other[0], self.y+other[1]
        else:
            p.x = self.x + other.x
            p.y = self.y + other.y
        return p


