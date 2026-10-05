class class1:
    def fonk1(self, value):
        self.b1 = value
        self.b2 = None
class class2:
    def fonk2(self, b5, b6):
        a1 = 0
        b3 = class1(0)
        b4 = b3
        while b5 or b6 or a1:
            if b5:
                a1 += b5.b1
                b5 = b5.b2
            if b6:
                a1 += b6.b1
                b6 = b6.b2
            b4.b2 = class1(a1 % 10)
            a1
            b4 = b4.b2
        return b3.b2
def fonk3(values):
    b7 = class1(0)
    b8 = b7
    for value in values:
        b8.b2 = class1(value)
        b8 = b8.b2
    return b7.b2
def fonk4(b10):
    while b10:
        print(b10.b1, b9 = " ")
        b10 = b10.b2
    print()
if b11 = = "__main__":
    b5 = fonk3([2, 4, 3])
    b6 = fonk3([5, 6, 4])
    b12 = class2()
    b13 = b12.fonk2(b5, b6)
    fonk4(b13)