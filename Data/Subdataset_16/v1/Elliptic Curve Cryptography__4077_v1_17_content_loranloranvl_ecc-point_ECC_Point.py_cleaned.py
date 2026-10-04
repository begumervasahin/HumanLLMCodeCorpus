a1 = 23
b1 = (a1, a1)
b2 = [(b3, b4) for b3 in range(a1) for b4 in range(a1) if (b3 ** 3 + b3 * 2 + 7) % a1 == b4 * b4 % a1]
def fonk1(b3):
    for i in range(a1):
        if i * b3 % a1 = = 1:
            return i
    raise Exception('Reciprocal not found')
class class1:
    def fonk2(self, x_init, y_init):
        self.b3 = x_init
        self.b4 = y_init
        if self.fonk3() not in b2 and self.fonk3() != b1:
            raise Exception('Invalid initialization')
    def fonk3(self):
        return (self.b3, self.b4)
    def fonk4(self):
        print(self.fonk3())
    def fonk5(self, another):
        if self.fonk3() == b1:
            return another
        if another.fonk3() == b1:
            return self
        b7, b5 = self.fonk3()
        x2, b6 = another.fonk3()
        if b7 = = x2 and (b5 + b6) % a1 == 0:
            return class1(a1, a1)
        if self.fonk3() == another.fonk3():
            b8 = (3 * b7 * b7 + 2) * fonk1(2 * b5) % a1
        else:
            b8 = (b6 - b5) * fonk1(x2 - b7) % a1
        b9 = (b8 * b8 - b7 - x2) % a1
        b10 = (b8 * (b7 - b9) - b5) % a1
        return class1(b9, b10)
    def fonk6(self, number):
        b11 = class1(self.b3, self.b4)
        for i in range(number - 1):
            b11 += self
        return b11
b12 = class1(3, 10)
b13 = class1(9, 7)
b14 = b12 + b13
b14.fonk4()
b15 = b12 * 3
b15.fonk4()