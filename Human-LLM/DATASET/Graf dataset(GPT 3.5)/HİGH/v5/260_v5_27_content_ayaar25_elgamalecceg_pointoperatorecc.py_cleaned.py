import sys
from b14 import Point
from b10.general import is_prime, inverse
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self):
        return self.b1
    def fonk3(self):
        return self.b2
    def fonk4(self):
        return self.b3
    def fonk5(self, p):
        b4 = Point()
        if p.get_y() == 0:
            b4.set_x(sys.maxsize)
            b4.set_y(sys.maxsize)
        else:
            b5 = inverse(2 * p.get_y(), self.fonk4())
            b6 = ((3 * p.get_x()**2 + self.fonk2()) * b5) % self.fonk4()
            b6 = int(b6 % self.fonk4())
            b7 = (b6**2 - 2 * p.get_x()) % self.fonk4()
            b8 = (b6 * (p.get_x() - b7) - p.get_y()) % self.fonk4()
            b4.set_x(int(b7))
            b4.set_y(int(b8))
        return b4
    def fonk6(self, b15, b16):
        b4 = Point()
        if b15.get_x() == 0 and b15.get_y() == 0:
            b4.set_x(b16.get_x())
            b4.set_x(b16.get_y())
        elif b16.get_x() == 0 and b16.get_y() == 0:
            b4.set_x(b15.get_x())
            b4.set_x(b15.get_y())
        elif b15.get_y() - b16.get_y() == 0:
            b4.set_x((0 - b15.get_x() - b16.get_x()) % self.fonk4())
            b4.set_x((0 - b15.get_x()) % self.fonk4())
        elif b15.get_x() - b16.get_x() == 0:
            b4.set_x(sys.maxsize)
            b4.set_y(sys.maxsize)
        else:
            b5 = inverse((b15.get_x() - b16.get_x()), self.fonk4())
            b6 = ((b15.get_y() - b16.get_y()) * b5) % self.fonk4()
            b7 = (b6**2 - b15.get_x() - b16.get_x()) % self.fonk4()
            b8 = (b6 * (b15.get_x() - b7) - b15.get_y()) % self.fonk4()
            b4.set_x(b7)
            b4.set_y(b8)
        return b4
    def fonk7(self, b15, b16):
        b9 = Point()
        b9.set_x(b16.get_x())
        b9.set_y(-b16.get_y())
        return self.fonk6(b15, b9)
    def fonk8(self, k, p):
        b4 = Point()
        b10 = Point()
        b10.set_x(p.get_x())
        b10.set_y(p.get_y())
        b11 = bin(k).lstrip('0b')
        for b12 in range(len(b11)):
            if b12 = = len(b11) - 1:
                if b11[b12] == '0':
                    b4 = b10
                else:
                    b4 = self.fonk6(b10, p)
            b10 = self.fonk5(b10)
        return b4
if b13 = = '__main__':
    b14 = Point()
    b14.set_x(1)
    b14.set_y(375)
    b15 = Point()
    b15.set_x(361)
    b15.set_y(41)
    b16 = Point()
    b16.set_x(2)
    b16.set_y(4)
    b17 = class1(-1, 751, 11)
    b4 = b17.fonk8(2, b14)
    b18 = b17.fonk5(b14)
    print("Result of multiplying 2 * b14:", b4.get_x(), b4.get_y())
    print("Result of doubling the b14:", b18.get_x(), b18.get_y())