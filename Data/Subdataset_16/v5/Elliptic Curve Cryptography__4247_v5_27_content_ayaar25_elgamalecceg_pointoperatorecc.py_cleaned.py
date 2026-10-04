import sys
from b15 import Point
from b11.general import is_prime, inverse
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
        return Point(int(b6), int(b7))
    def fonk3(self, b8, b16):
        if b8.is_at_infinity():
            return Point(b16.get_x(), b16.get_y())
        if b16.is_at_infinity():
            return Point(b8.get_x(), b8.get_y())
        if b8 = = b16:
            return self.fonk2(b8)
        if b8.get_x() == b16.get_x():
            return Point(sys.maxsize, sys.maxsize)
        b4 = inverse(b8.get_x() - b16.get_x(), self.b3)
        b5 = ((b8.get_y() - b16.get_y()) * b4) % self.b3
        b6 = (b5 ** 2 - b8.get_x() - b16.get_x()) % self.b3
        b7 = (b5 * (b8.get_x() - b6) - b8.get_y()) % self.b3
        return Point(int(b6), int(b7))
    def fonk4(self, b8, b16):
        b9 = Point(b16.get_x(), -b16.get_y())
        return self.fonk3(b8, b9)
    def fonk5(self, k, p):
        b10 = Point()
        b11 = Point(p.get_x(), p.get_y())
        b12 = bin(k)[2:]
        for b13 in b12:
            if b13 = = '1':
                b10 = self.fonk3(b10, b11)
            b11 = self.fonk2(b11)
        return b10
if b14 = = '__main__':
    b15 = Point(1, 375)
    b8 = Point(361, 41)
    b16 = Point(2, 4)
    b17 = class1(-1, 751, 11)
    b10 = b17.fonk5(2, b15)
    b18 = b17.fonk2(b15)
    print(f"Multiplication Result: ({b10.get_x()}, {b10.get_y()})")
    print(f"Doubling Result: ({b18.get_x()}, {b18.get_y()})")