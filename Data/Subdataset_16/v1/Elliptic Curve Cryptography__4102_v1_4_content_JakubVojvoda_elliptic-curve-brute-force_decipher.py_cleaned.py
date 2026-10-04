import sys
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self, b5):
        return self.b1 = = b5.b1 and self.b2 == b5.b2
class class2:
    def fonk3(self, b3, b4, b5):
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk4(self, b5):
        b6 = self.fonk5(b5.b2 * b5.b2)
        b7 = self.fonk5(b5.b1 * b5.b1 * b5.b1 + self.b3 * b5.b1 + self.b4)
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
    def fonk7(self, b5, b11):
        b14 = class1(0, 0)
        if b5.fonk2(b14):
            return b11
        if b11.fonk2(b14):
            return b5
        if b5.fonk2(b11):
            if b5.b2 != 0:
                b15 = self.fonk5(self.fonk5(3 * b5.b1 * b5.b1 + self.b3) * self.fonk6(b17 * b5.b2))
                b14.b1 = self.fonk5(b15 * b15 - b17 * b5.b1)
                b14.b2 = self.fonk5(b15 * (b5.b1 - b14.b1) - b5.b2)
        else:
            if b11.b1 - b5.b1 != 0:
                b15 = self.fonk5(self.fonk5(b11.b2 - b5.b2) * self.fonk6(b11.b1 - b5.b1))
                b14.b1 = self.fonk5(b15 * b15 - b5.b1 - b11.b1)
                b14.b2 = self.fonk5(b15 * (b5.b1 - b14.b1) - b5.b2)
        return b14
    def fonk8(self, b5):
        return self.fonk7(b5, b5)
    def fonk9(self, b5, b16):
        if b16 = = 0:
            return class1(0, 0)
        elif b16 = = 1:
            return b5
        elif b16 % b17 = = 1:
            return self.fonk7(b5, self.fonk9(b5, b16 - 1))
        else:
            return self.fonk9(self.fonk8(b5), b16
class class3:
    def fonk10(self, b18, b5, b11, b16):
        self.b18 = b18
        self.b5 = b5
        self.b11 = b11
        self.b16 = b16
    def fonk11(self):
        b14 = class1(0, 0)
        for d in range(1, self.b16):
            b14 = self.b18.fonk7(self.b5, b14)
            if not self.b18.fonk4(b14):
                return 0
            if b14.fonk2(self.b11):
                return d
        return 0
def fonk12():
    b3 = -0x3
    b4 = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
    b5 = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
    b19 = class1(
        0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,
        0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5
    )
    b20 = class1(
        0x52910a011565810be90d03a299cb55851bab33236b7459b21db82b9f5c1874fe,
        0xe3d03339f660528d511c2b1865bcdfd105490ffc4c597233dd2b2504ca42a562
    )
    b18 = class2(b3, b4, b5)
    if not b18.fonk4(b19) or not b18.fonk4(b20):
        return 0
    b21 = class3(b18, b19, b20, b5)
    return b21.fonk11()
if b22 = = "__main__":
    b23 = fonk12()
    print(b23)