class class1:
    def fonk1(self, b2, b1):
        self.b2, self.b1 = b2, b1
    def fonk2(self, other_point):
        return self.b2 = = other_point.b2 and self.b1 == other_point.b1
class class2:
    def fonk3(self, b17, b18, b3):
        self.b17, self.b18, self.b3 = b17, b18, b3
    def fonk4(self, point):
        b4 = self.fonk5(point.b1 * point.b1)
        b5 = self.fonk5(point.b2 * point.b2 * point.b2 + self.b17 * point.b2 + self.b18)
        b6 = 4 * self.b17 * self.b17 * self.b17 + 27 * self.b18 * self.b18
        return b4 = = b5 and b6 != 0
    def fonk5(self, b2):
        return b2 % self.b3
    def fonk6(self, b2):
        b11, b7 = 0, 1
        b10, b8 = self.b3, b2
        while b10 != 0:
            b9 = b8
            b8, b10 = b10, b8 - b9 * b10
            b7, b11 = b11, b7 - b9 * b11
        return b7 % self.b3
    def fonk7(self, b3, b9):
        b12 = class1(0, 0)
        if b3.fonk2(b12):
            return b9
        if b9.fonk2(b12):
            return b3
        if b3.fonk2(b9):
            if b3.b1 != 0:
                b13 = self.fonk5(self.fonk5(3 * b3.b2 * b3.b2 + self.b17) * self.fonk6(b15 * b3.b1))
                b12.b2 = self.fonk5(b13 * b13 - b15 * b3.b2)
                b12.b1 = self.fonk5(b13 * (b3.b2 - b12.b2) - b3.b1)
        else:
            if b9.b2 - b3.b2 != 0:
                b13 = self.fonk5(self.fonk5(b9.b1 - b3.b1) * self.fonk6(b9.b2 - b3.b2))
                b12.b2 = self.fonk5(b13 * b13 - b3.b2 - b9.b2)
                b12.b1 = self.fonk5(b13 * (b3.b2 - b12.b2) - b3.b1)
        return b12
    def fonk8(self, b3):
        return self.fonk7(b3, b3)
    def fonk9(self, b3, b14):
        if b14 = = 0:
            return class1(0, 0)
        elif b14 = = 1:
            return b3
        elif b14 % b15 = = 1:
            return self.fonk7(b3, self.fonk9(b3, b14 - 1))
        else:
            return self.fonk9(self.fonk8(b3), b14 / b15)
class class3:
    def fonk10(self, b21, b3, b9, b14):
        self.b21, self.b3, self.b9, self.b14 = b21, b3, b9, b14
    def fonk11(self):
        b12 = class1(0, 0)
        for d in range(1, self.b14):
            b12 = self.b21.fonk7(self.b3, b12)
            if not self.b21.fonk4(b12):
                return 0
            if b12.fonk2(self.b9):
                return d
        return 0
def fonk12(b16 = None):
    b17 = -0x3
    b18 = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
    b3 = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
    b19 = class1(
        0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,
        0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5
    )
    b20 = class1(
        0x52910a011565810be90d03a299cb55851bab33236b7459b21db82b9f5c1874fe,
        0xe3d03339f660528d511c2b1865bcdfd105490ffc4c597233dd2b2504ca42a562
    )
    b21 = class2(b17, b18, b3)
    if not b21.fonk4(b19) or not b21.fonk4(b20):
        return 0
    b22 = class3(b21, b19, b20, b3)
    return b22.fonk11()
if b23 = = "__main__":
    b24 = fonk12()
    print(b24)