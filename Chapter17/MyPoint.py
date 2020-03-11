class Point:
    """Represents a point in 2-D space."""
    def __add__(self, other):
        p = Point()
        if isinstance(other, tuple):
            p.x, p.y = self.x+other[0], self.y+other[1]
        else:
            p.x = self.x + other.x
            p.y = self.y + other.y
        return p


