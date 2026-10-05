class Point:
    def __init__(self, x_coord, y_coord, z_coord, modulus):
        self.x = x_coord
        self.y = y_coord
        self.z = z_coord
        self.p = modulus
    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"
    def __eq__(self, other_point):
        return (
            self.x == other_point.x
            and self.y == other_point.y
            and self.z == other_point.z
            and self.p == other_point.p
        )
    def negate(self):
        self.y = (-self.y) % self.p
        return self
    @staticmethod
    def make_point(x_coord, y_coord, z_coord, modulus):
        return Point(x_coord, y_coord, z_coord, modulus)
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
