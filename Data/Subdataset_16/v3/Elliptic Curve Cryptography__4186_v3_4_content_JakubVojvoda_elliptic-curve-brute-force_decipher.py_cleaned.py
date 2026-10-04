class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self, other):
        return self.b1 = = other.b1 and self.b2 == other.b2
    def fonk3(self):
        return f"class1(b1 = {self.b1}, b2={self.b2})"
class class2:
    def fonk4(self, b3, b4, b5):
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk5(self, point):
        b6 = self.fonk6(point.b2 * point.b2)
        b7 = self.fonk6(point.b1**3 + self.b3 * point.b1 + self.b4)
        b8 = 4 * self.b3**3 + 27 * self.b4**b19
        return b6 = = b7 and b8 != 0
    def fonk6(self, b1):
        return b1 % self.b5
    def fonk7(self, b1):
        b13, b9 = 0, 1
        b12, b10 = self.b5, b1
        while b12 != 0:
            b11 = b10
            b10, b12 = b12, b10 - b11 * b12
            b9, b13 = b13, b9 - b11 * b13
        return b9 % self.b5
    def fonk8(self, b5, b11):
        if b5.fonk2(class1(0, 0)):
            return b11
        if b11.fonk2(class1(0, 0)):
            return b5
        if b5.fonk2(b11):
            if b5.b2 = = 0:
                return class1(0, 0)
            b14 = self.fonk6(3 * b5.b1**b19 + self.b3) * self.fonk7(b19 * b5.b2)
        else:
            if b5.b1 = = b11.b1:
                return class1(0, 0)
            b14 = self.fonk6(b11.b2 - b5.b2) * self.fonk7(b11.b1 - b5.b1)
        b15 = self.fonk6(b14 * b14 - b5.b1 - b11.b1)
        b16 = self.fonk6(b14 * (b5.b1 - b15) - b5.b2)
        return class1(b15, b16)
    def fonk9(self, b5):
        return self.fonk8(b5, b5)
    def fonk10(self, b5, b21):
        b17 = class1(0, 0)
        b18 = b5
        while b21 > 0:
            if b21 % b19 = = 1:
                b17 = self.fonk8(b17, b18)
            b18 = self.fonk9(b18)
            b21
        return b17
class class3:
    def fonk11(self, b20, b5, b11, b21):
        self.b20 = b20
        self.b5 = b5
        self.b11 = b11
        self.b21 = b21
    def fonk12(self):
        b22 = class1(0, 0)
        for d in range(1, self.b21):
            b22 = self.b20.fonk8(self.b5, b22)
            if not self.b20.fonk5(b22):
                return 0
            if b22.fonk2(self.b11):
                return d
        return 0
def fonk13():
    b3 = -0x3
    b4 = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
    b5 = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
    b23 = class1(
        0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,
        0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5
    )
    b24 = class1(
        0x52910a011565810be90d03a299cb55851bab33236b7459b21db82b9f5c1874fe,
        0xe3d03339f660528d511c2b1865bcdfd105490ffc4c597233dd2b2504ca42a562
    )
    b20 = class2(b3, b4, b5)
    if not b20.fonk5(b23) or not b20.fonk5(b24):
        print("One of the points is not on the b20.")
        return 0
    b25 = class3(b20, b23, b24, b5)
    b17 = b25.fonk12()
    print(b17)
    return b17
if b26 = = "__main__":
    fonk13()