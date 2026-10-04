import sys
from b14 import Point
from b10.general import is_prime, inverse
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self, p):
        if p.get_y() == 0:
            return Point(sys.maxsize, sys.maxsize)
        b4 = inverse(2 * p.get_y(), self.b3)
        b5 = ((3 * (p.get_x() ** 2) + self.b1) * b4) % self.b3
        b6 = (b5 ** 2 - 2 * p.get_x()) % self.b3
        b7 = (b5 * (p.get_x() - b6) - p.get_y()) % self.b3
        return Point(b6, b7)
    def fonk3(self, b15, b16):
        if b15.get_x() == 0 and b15.get_y() == 0:
            return Point(b16.get_x(), b16.get_y())
        if b16.get_x() == 0 and b16.get_y() == 0:
            return Point(b15.get_x(), b15.get_y())
        if b15.get_x() == b16.get_x() and b15.get_y() == b16.get_y():
            return self.fonk2(b15)
        if b15.get_x() == b16.get_x():
            return Point(sys.maxsize, sys.maxsize)
        b4 = inverse(b15.get_x() - b16.get_x(), self.b3)
        b5 = ((b15.get_y() - b16.get_y()) * b4) % self.b3
        b6 = (b5 ** 2 - b15.get_x() - b16.get_x()) % self.b3
        b7 = (b5 * (b15.get_x() - b6) - b15.get_y()) % self.b3
        return Point(b6, b7)
    def fonk4(self, b15, b16):
        b8 = Point(b16.get_x(), -b16.get_y())
        return self.fonk3(b15, b8)
    def fonk5(self, k, p):
        b9 = Point()
        b10 = Point(p.get_x(), p.get_y())
        b11 = bin(k)[2:]
        for b12 in b11:
            if b12 = = '1':
                b9 = self.fonk3(b9, b10)
            b10 = self.fonk2(b10)
        return b9
if b13 = = '__main__':
    b14 = Point(1, 375)
    b15 = Point(361, 41)
    b16 = Point(2, 4)
    b17 = class1(-1, 751, 11)
    b9 = b17.fonk5(2, b14)
    b18 = b17.fonk2(b14)
    print(f"Multiplication Result: ({b9.get_x()}, {b9.get_y()})")
    print(f"Doubling Result: ({b18.get_x()}, {b18.get_y()})")