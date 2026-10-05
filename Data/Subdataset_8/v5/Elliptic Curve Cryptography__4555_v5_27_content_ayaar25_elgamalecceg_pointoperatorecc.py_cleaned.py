import sys
from point import Point
from base.general import is_prime, inverse
class PointOperatorECC:
    def __init__(self, A, B, P):
        self.A = A
        self.B = B
        self.P = P
    def get_A(self):
        return self.A
    def get_B(self):
        return self.B
    def get_P(self):
        return self.P
    def double_point(self, p):
        result = Point()
        if p.get_y() == 0:
            result.set_x(sys.maxsize)
            result.set_y(sys.maxsize)
        else:
            inv = inverse(2 * p.get_y(), self.get_P())
            lamda = ((3 * p.get_x()**2 + self.get_A()) * inv) % self.get_P()
            lamda = int(lamda % self.get_P())
            xr = (lamda**2 - 2 * p.get_x()) % self.get_P()
            yr = (lamda * (p.get_x() - xr) - p.get_y()) % self.get_P()
            result.set_x(int(xr))
            result.set_y(int(yr))
        return result
    def add(self, p1, p2):
        result = Point()
        if p1.get_x() == 0 and p1.get_y() == 0:
            result.set_x(p2.get_x())
            result.set_x(p2.get_y())
        elif p2.get_x() == 0 and p2.get_y() == 0:
            result.set_x(p1.get_x())
            result.set_x(p1.get_y())
        elif p1.get_y() - p2.get_y() == 0:
            result.set_x((0 - p1.get_x() - p2.get_x()) % self.get_P())
            result.set_x((0 - p1.get_x()) % self.get_P())
        elif p1.get_x() - p2.get_x() == 0:
            result.set_x(sys.maxsize)
            result.set_y(sys.maxsize)
        else:
            inv = inverse((p1.get_x() - p2.get_x()), self.get_P())
            lamda = ((p1.get_y() - p2.get_y()) * inv) % self.get_P()
            xr = (lamda**2 - p1.get_x() - p2.get_x()) % self.get_P()
            yr = (lamda * (p1.get_x() - xr) - p1.get_y()) % self.get_P()
            result.set_x(xr)
            result.set_y(yr)
        return result
    def minus(self, p1, p2):
        temp = Point()
        temp.set_x(p2.get_x())
        temp.set_y(-p2.get_y())
        return self.add(p1, temp)
    def multiply(self, k, p):
        result = Point()
        base = Point()
        base.set_x(p.get_x())
        base.set_y(p.get_y())
        bin_k = bin(k).lstrip('0b')
        for i in range(len(bin_k)):
            if i == len(bin_k) - 1:
                if bin_k[i] == '0':
                    result = base
                else:
                    result = self.add(base, p)
            base = self.double_point(base)
        return result
if __name__ == '__main__':
    point = Point()
    point.set_x(1)
    point.set_y(375)
    p1 = Point()
    p1.set_x(361)
    p1.set_y(41)
    p2 = Point()
    p2.set_x(2)
    p2.set_y(4)
    op = PointOperatorECC(-1, 751, 11)
    result = op.multiply(2, point)
    result_double = op.double_point(point)
    print("Result of multiplying 2 * point:", result.get_x(), result.get_y())
    print("Result of doubling the point:", result_double.get_x(), result_double.get_y())