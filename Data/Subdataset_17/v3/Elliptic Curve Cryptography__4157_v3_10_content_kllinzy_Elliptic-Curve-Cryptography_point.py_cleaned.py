class Point:
    def __init__(self, x, y, z, p):
        self.x = x
        self.y = y
        self.z = z
        self.p = p
    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z and self.p == other.p
    @staticmethod
    def make_point(x, y, z, p):
        return Point(x, y, z, p)
    def negate(self):
        return Point(self.x, (-self.y) % self.p, self.z, self.p)
if __name__ == "__main__":
    point1 = Point(1, 2, 3, 7)
    point2 = Point.make_point(1, 2, 3, 7)
    print(f"Point 1: {point1}")
    print(f"Point 2: {point2}")
    print(f"Point 1 == Point 2: {point1 == point2}")
    negated_point = point1.negate()
    print(f"Negated Point 1: {negated_point}")