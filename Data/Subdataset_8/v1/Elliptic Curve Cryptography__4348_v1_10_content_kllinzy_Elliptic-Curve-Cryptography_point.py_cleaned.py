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
    def negate(self):
        self.y = (-self.y) % self.p
        return self
    @staticmethod
    def make_point(x, y, z, p):
        return Point(x, y, z, p)
point1 = Point(1, 2, 3, 5)
print(point1)
point2 = Point.make_point(4, 5, 6, 7)
print(point2)
point3 = Point(1, 2, 3, 5)
print(point1 == point3)
point4 = Point(1, 2, 4, 5)
print(point1 == point4)
point1.negate()
print(point1)
