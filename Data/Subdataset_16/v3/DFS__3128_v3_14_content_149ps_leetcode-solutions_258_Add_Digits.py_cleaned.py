class class1:
    def fonk1(self, b1: int) -> int:
        while b1 >= 10:
            b1 = sum(int(digit) for digit in str(b1))
        return b1
b2 = class1()
print(b2.fonk1(38))
print(b2.fonk1(123))
print(b2.fonk1(0))
