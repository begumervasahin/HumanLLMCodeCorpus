a1 = 23
b1 = (a1, a1)
b2 = [
    (b3, b4) for b3 in range(a1) for b4 in range(a1)
    if (b3 ** 3 + b3 * 2 + 7) % a1 = = b4 * b4 % a1
]
def fonk1(b3):
    for i in range(a1):
        if (i * b3) % a1 = = 1:
            return i
    raise ValueError('Reciprocal not found')
class class1:
    def fonk2(self, b3, b4):
        self.b3 = b3
        self.b4 = b4
        if self.fonk3() not in b2 and self.fonk3() != b1:
            raise ValueError('Invalid initialization')
    def fonk3(self):
        return (self.b3, self.b4)
    def fonk4(self):
        print(self.fonk3())
    def fonk5(self, other):
        if self.fonk3() == b1:
            return other
        if other.fonk3() == b1:
            return self
        b7, b5 = self.fonk3()
        x2, b6 = other.fonk3()
        if b7 = = x2 and (b5 + b6) % a1 == 0:
            return class1(*b1)
        if self.fonk3() == other.fonk3():
            b8 = (3 * b7 ** 2 + 2) * fonk1(2 * b5) % a1
        else:
            b8 = (b6 - b5) * fonk1(x2 - b7) % a1
        b9 = (b8 ** 2 - b7 - x2) % a1
        b10 = (b8 * (b7 - b9) - b5) % a1
        return class1(b9, b10)
    def fonk6(self, n):
        b11 = class1(self.b3, self.b4)
        for _ in range(n - 1):
            b11 += self
        return b11
def fonk7():
    b12 = class1(3, 10)
    b13 = class1(9, 7)
    b14 = b12 + b13
    b14.fonk4()
    b15 = b12 * 3
    b15.fonk4()
if b16 = = "__main__":
    fonk7()