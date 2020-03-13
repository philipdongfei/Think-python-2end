class LinearMap:
    def __init__(self):
        self.items = []
    def add(self, k, v):
        self.items.append((k, v))
    def get(self, k):
        for key, val in self.items:
            if key == k:
                return val
        raise keyError

