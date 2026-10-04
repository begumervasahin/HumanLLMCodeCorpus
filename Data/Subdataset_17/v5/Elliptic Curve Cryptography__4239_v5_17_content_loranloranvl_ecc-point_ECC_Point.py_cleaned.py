BASE = 23
INFINITE_POINT = (BASE, BASE)
F_BASE = [(x, y) for x in range(BASE) for y in range(BASE) if (x**3 + x*2 + 7) % BASE == y*y % BASE]
def get_reciprocal(x):
    for i in range(BASE):
        if i * x % BASE == 1:
            return i
    raise Exception('Reciprocal not found')
class ECC_Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        if self.coords() not in F_BASE and self.coords() != INFINITE_POINT:
            raise Exception('Invalid initialization')
    def coords(self):
        return (self.x, self.y)
    def show_coords(self):
        print(self.coords())
    def __add__(self, other):
        if self.coords() == INFINITE_POINT:
            return other
        if other.coords() == INFINITE_POINT:
            return self
        x1, y1 = self.x, self.y
        x2, y2 = other.x, other.y
        if x1 == x2 and y1 == -y2:
            return ECC_Point(BASE, BASE)
        if self == other:
            lamda = (3 * x1 * x1 + 2) * get_reciprocal(2 * y1) % BASE
        else:
            lamda = (y2 - y1) * get_reciprocal(x2 - x1) % BASE
        x3 = (lamda * lamda - x1 - x2) % BASE
        y3 = (lamda * (x1 - x3) - y1) % BASE
        return ECC_Point(x3, y3)
    def __mul__(self, n):
        result = self
        for _ in range(n - 1):
            result = result + self
        return result