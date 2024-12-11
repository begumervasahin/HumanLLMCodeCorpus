class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self, other_point):
        return self.b1 = = other_point.b1 and self.b2 == other_point.b2
class class2:
    def fonk3(self, b3, b4, b5):
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk4(self, point):
        b6 = self.fonk5(point.b2 * point.b2)
        b7 = self.fonk5(point.b1 * point.b1 * point.b1 + self.b3 * point.b1 + self.b4)
        b8 = 4 * self.b3 * self.b3 * self.b3 + 27 * self.b4 * self.b4
        return b6 = = b7 and b8 != 0
    def fonk5(self, b1):
        return b1 % self.b5
    def fonk6(self, b1):
        b13, b9 = 0, 1
        b12, b10 = self.b5, b1
        while b12 != 0:
            b11 = b10
            b10, b12 = b12, b10 - b11 * b12
            b9, b13 = b13, b9 - b11 * b13
        return b9 % self.b5
    def fonk7(self, point1, point2):
        b14 = class1(0, 0)
        if point1.fonk2(b14):
            return point2
        if point2.fonk2(b14):
            return point1
        if point1.fonk2(point2):
            if point1.b2 != 0:
                b15 = self.fonk5((3 * point1.b1 * point1.b1 + self.b3) * self.fonk6(b17 * point1.b2))
                b14.b1 = self.fonk5(b15 * b15 - b17 * point1.b1)
                b14.b2 = self.fonk5(b15 * (point1.b1 - b14.b1) - point1.b2)
        else:
            if point2.b1 - point1.b1 != 0:
                b15 = self.fonk5((point2.b2 - point1.b2) * self.fonk6(point2.b1 - point1.b1))
                b14.b1 = self.fonk5(b15 * b15 - point1.b1 - point2.b1)
                b14.b2 = self.fonk5(b15 * (point1.b1 - b14.b1) - point1.b2)
        return b14
    def fonk8(self, point):
        return self.fonk7(point, point)
    def fonk9(self, point, b16):
        if b16 = = 0:
            return class1(0, 0)
        elif b16 = = 1:
            return point
        elif b16 % b17 = = 1:
            return self.fonk7(point, self.fonk9(point, b16 - 1))
        else:
            return self.fonk9(self.fonk8(point), b16 / b17)
class class3:
    def fonk10(self, b18, b19, b20, b21):
        self.b18 = b18
        self.b19 = b19
        self.b20 = b20
        self.b21 = b21
    def fonk11(self):
        b14 = class1(0, 0)
        for d in range(1, self.b21):
            b14 = self.b18.fonk7(self.b19, b14)
            if not self.b18.fonk4(b14):
                return 0
            if b14.fonk2(self.b20):
                return d
        return 0
def fonk12():
    a1 = -3
    b22 = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
    b5 = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
    b23 = class1(
        0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,
        0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5
    )
    b24 = class1(
        0x52910a011565810be90d03a299cb55851bab33236b7459b21db82b9f5c1874fe,
        0xe3d03339f660528d511c2b1865bcdfd105490ffc4c597233dd2b2504ca42a562
    )
    b25 = class2(a1, b22, b5)
    if not b25.fonk4(b23) or not b25.fonk4(b24):
        return 0
    b26 = class3(b25, b23, b24, b5)
    return b26.fonk11()
if b27 = = "__main__":
    b28 = fonk12()
    print(b28)