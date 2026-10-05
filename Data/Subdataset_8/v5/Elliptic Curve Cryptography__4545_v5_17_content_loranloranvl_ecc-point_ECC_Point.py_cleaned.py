BASE = 23
infinite_point = (BASE, BASE)
F_BASE = [(x, y) for x in range(BASE) for y in range(BASE) if (x ** 3 + x * 2 + 7) % BASE == y * y % BASE]
def get_reciprocal(x):
    for i in range(BASE):
        if i * x % BASE == 1:
            return i
    raise Exception('Reciprocal not found')
class ECC_Point:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init
        if self.val() not in F_BASE and self.val() != infinite_point:
            raise Exception('Invalid initialization')
    def val(self):
        return (self.x, self.y)
    def show_val(self):
        print(self.val())
    def __add__(self, other):
        if self.val() == infinite_point:
            return other
        if other.val() == infinite_point:
            return self
        x1, y1 = self.x, self.y
        x2, y2 = other.x, other.y
        if x1 == x2 and y1 == -y2:
            return ECC_Point(BASE, BASE)
        if self == other:
            lamda = (3 * x1 * x1 + 2) * get_reciprocal(2 * y2) % BASE
        else:
            lamda = (y2 - y1) * get_reciprocal(x2 - x1) % BASE
        x3 = (lamda * lamda - x1 - x2) % BASE
        y3 = (lamda * (x1 - x3) - y1) % BASE
        return ECC_Point(x3, y3)
    def __mul__(self, number):
        result = self
        for _ in range(number - 1):
            result += self
        return result