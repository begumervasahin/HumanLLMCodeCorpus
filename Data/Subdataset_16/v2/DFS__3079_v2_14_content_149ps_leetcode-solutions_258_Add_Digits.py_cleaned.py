class class1:
    def fonk1(self, num: int) -> int:
        b1 = num
        while b1 >= 10:
            a1 = 0
            while b1 > 0:
                a1 += b1 % 10
                b1
            b1 = a1
        return b1
b2 = class1()
print(b2.fonk1(38))
print(b2.fonk1(123))
print(b2.fonk1(0))
