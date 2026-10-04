import sys
from point import Point
from base.general import is_prime, inverse
class PointOperatorECC:
    def __init__(self, A, B, P):
        self.A = A
        self.B = B
        self.P = P
    def double_point(self, p):
        if p.get_y() == 0:
            return Point(sys.maxsize, sys.maxsize)
        inv = inverse(2 * p.get_y(), self.P)
        lamda = ((3 * (p.get_x() ** 2) + self.A) * inv) % self.P
        xr = (lamda ** 2 - 2 * p.get_x()) % self.P
        yr = (lamda * (p.get_x() - xr) - p.get_y()) % self.P
        return Point(int(xr), int(yr))
    def add(self, p1, p2):
        if p1.is_at_infinity():
            return Point(p2.get_x(), p2.get_y())
        if p2.is_at_infinity():
            return Point(p1.get_x(), p1.get_y())
        if p1 == p2:
            return self.double_point(p1)
        if p1.get_x() == p2.get_x():
            return Point(sys.maxsize, sys.maxsize)
        inv = inverse(p1.get_x() - p2.get_x(), self.P)
        lamda = ((p1.get_y() - p2.get_y()) * inv) % self.P
        xr = (lamda ** 2 - p1.get_x() - p2.get_x()) % self.P
        yr = (lamda * (p1.get_x() - xr) - p1.get_y()) % self.P
        return Point(int(xr), int(yr))
    def subtract(self, p1, p2):
        neg_p2 = Point(p2.get_x(), -p2.get_y())
        return self.add(p1, neg_p2)
    def multiply(self, k, p):
        result = Point()
        base = Point(p.get_x(), p.get_y())
        bin_k = bin(k)[2:]
        for bit in bin_k:
            if bit == '1':
                result = self.add(result, base)
            base = self.double_point(base)
        return result
if __name__ == '__main__':
    point = Point(1, 375)
    p1 = Point(361, 41)
    p2 = Point(2, 4)
    op = PointOperatorECC(-1, 751, 11)
    result = op.multiply(2, point)
    result_double = op.double_point(point)
    print(f"Multiplication Result: ({result.get_x()}, {result.get_y()})")
    print(f"Doubling Result: ({result_double.get_x()}, {result_double.get_y()})")