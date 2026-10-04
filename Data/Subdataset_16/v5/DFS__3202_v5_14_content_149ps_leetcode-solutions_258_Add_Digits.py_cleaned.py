class class1:
    def fonk1(self, b1: int) -> int:
        while b1 >= 10:
            b1 = self.fonk2(b1)
        return b1
    def fonk2(self, b1: int) -> int:
        a1 = 0
        while b1 > 0:
            a1 += b1 % 10
            b1
        return a1
b2 = class1()
print(b2.fonk1(38))
print(b2.fonk1(123))
print(b2.fonk1(0))
