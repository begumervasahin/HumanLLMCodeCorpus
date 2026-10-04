class class1:
    def fonk1(self, x):
        self.b1 = x
        self.b2 = None
class class2:
    def fonk2(self, b8, b9):
        a1 = 0
        b3 = class1(0)
        b4 = b3
        while b8 or b9 or a1:
            b5 = b8.b1 if b8 else 0
            b6 = b9.b1 if b9 else 0
            a1, b7 = divmod(b5 + b6 + a1, 10)
            b4.b2 = class1(b7)
            b4 = b4.b2
            if b8: b8 = b8.b2
            if b9: b9 = b9.b2
        return b3.b2
def fonk3(b11):
    while b11:
        print(b11.b1, b10 = " -> " if b11.b2 else "\n")
        b11 = b11.b2
if b12 = = "__main__":
    b8 = class1(2)
    b8.b2 = class1(4)
    b8.b2.b2 = class1(3)
    b9 = class1(5)
    b9.b2 = class1(6)
    b9.b2.b2 = class1(4)
    b13 = class2()
    b14 = b13.fonk2(b8, b9)
    print("Result linked list:")
    fonk3(b14)