class EllipticCurve:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    @staticmethod
    def get_instance(a, b):
        return EllipticCurve(a, b)
    def __str__(self):
        return f"EllipticCurve(a={self.a}, b={self.b})"
class RationalPointInEC:
    def __init__(self, x=None, y=None, curve=None):
        self.x = x
        self.y = y
        self.curve = curve
    def __str__(self):
        if self.x is None or self.y is None:
            return "Point at Infinity"
        return f"({self.x}, {self.y})"
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.curve == other.curve
    def __add__(self, other):
        if self.x is None:
            return other
        if other.x is None:
            return self
        if self == other:
            return self.double()
        if self.x == other.x:
            return RationalPointInEC(curve=self.curve)
        m = (other.y - self.y) / (other.x - self.x)
        x3 = m ** 2 - self.x - other.x
        y3 = m * (self.x - x3) - self.y
        return RationalPointInEC(x3, y3, self.curve)
    def double(self):
        if self.y == 0:
            return RationalPointInEC(curve=self.curve)
        m = (3 * self.x ** 2 + self.curve.a) / (2 * self.y)
        x3 = m ** 2 - 2 * self.x
        y3 = m * (self.x - x3) - self.y
        return RationalPointInEC(x3, y3, self.curve)
    def __rmul__(self, k):
        result = RationalPointInEC(curve=self.curve)
        addend = self
        while k:
            if k & 1:
                result = result + addend
            addend = addend.double()
            k >>= 1
        return result
if __name__ == "__main__":
    curve = EllipticCurve.get_instance(0, -2)
    print(curve)
    o = RationalPointInEC(curve=curve)
    r1 = RationalPointInEC(-1, 1, curve)
    r2 = RationalPointInEC(2, 2, curve)
    print('Show values')
    print('o = ' + str(o))
    print('r1 = ' + str(r1))
    print('r2 = ' + str(r2))
    print('Show calculations')
    print('r1 + o = ' + str(r1 + o))
    print('r2 + r1 = ' + str(r2 + r1))
    print('2 * r1 = ' + str(2 * r1))
    print('4 * r1 == 3 * r1 + r1 is ' + str(4 * r1 == 3 * r1 + r1))