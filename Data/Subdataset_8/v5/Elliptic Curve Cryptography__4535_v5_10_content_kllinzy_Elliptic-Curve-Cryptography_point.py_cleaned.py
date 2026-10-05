class Point:
    def __init__(self, x: int, y: int, z: int, p: int) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.p = p
    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"
    def __eq__(self, other: 'Point') -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z and self.p == other.p
    @staticmethod
    def make_point(x: int, y: int, z: int, p: int) -> 'Point':
        return Point(x, y, z, p)
    def negate(self) -> 'Point':
        self.y = (-self.y) % self.p
        return self