class Point:
    def __init__(self, x, y, z, p):
        self.x = x
        self.y = y
        self.z = z
        self.p = p
    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z and self.p == other.p
    @staticmethod
    def make_point(x, y, z, p):
        return Point(x, y, z, p)
    def negate(self):
        self.y = (-self.y) % self.p
        return self