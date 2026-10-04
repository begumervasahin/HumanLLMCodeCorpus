class class1:
    def fonk1(self, value):
        self.b1 = value
        self.b2 = None
class class2:
    def fonk2(self, b6, b7):
        a1 = 0
        b3 = class1(0)
        b4 = b3
        while b6 or b7 or a1:
            b5 = a1
            if b6:
                b5 += b6.b1
                b6 = b6.b2
            if b7:
                b5 += b7.b1
                b7 = b7.b2
            a1, b1 = divmod(b5, 10)
            b4.b2 = class1(b1)
            b4 = b4.b2
        return b3.b2
def fonk3(b9):
    b8 = []
    while b9:
        b8.append(str(b9.b1))
        b9 = b9.b2
    print(" -> ".join(b8))
if b10 = = "__main__":
    b6 = class1(2)
    b6.b2 = class1(4)
    b6.b2.b2 = class1(3)
    b7 = class1(5)
    b7.b2 = class1(6)
    b7.b2.b2 = class1(4)
    print("Input:")
    print("b6: ", b11 = "")
    fonk3(b6)
    print("b7: ", b11 = "")
    fonk3(b7)
    b12 = class2()
    b13 = b12.fonk2(b6, b7)
    print("Output:")
    fonk3(b13)