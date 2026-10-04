class class1:
    def fonk1(self, x):
        self.b1 = x
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
def fonk3(b8):
    while b8:
        print(b8.b1, b7 = " -> " if b8.b2 else "\n")
        b8 = b8.b2
if b9 = = "__main__":
    b5 = class1(2)
    b5.b2 = class1(4)
    b5.b2.b2 = class1(3)
    b6 = class1(5)
    b6.b2 = class1(6)
    b6.b2.b2 = class1(4)
    print("Input:")
    print("b5: ", b7 = "")
    fonk3(b5)
    print("b6: ", b7 = "")
    fonk3(b6)
    b10 = class2()
    b11 = b10.fonk2(b5, b6)
    print("Output:")
    fonk3(b11)