class Point:
    def __init__(self, x, y, z, p):
        self.x = x
        self.y = y
        self.z = z
        self.p = p
    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    @staticmethod
    def make_point(x, y, z, p):
        return Point(x, y, z, p)
    def negate(self):
        self.y = (-1 * self.y) % self.p
        return self
if __name__ == "__main__":
    point1 = Point(1, 2, 3, 7)
    point2 = Point.make_point(1, 2, 3, 7)
    print(f"Point 1: {point1}")
    print(f"Point 2: {point2}")
    print(f"Point 1 == Point 2: {point1 == point2}")
    negated_point = point1.negate()
    print(f"Negated Point 1: {negated_point}")