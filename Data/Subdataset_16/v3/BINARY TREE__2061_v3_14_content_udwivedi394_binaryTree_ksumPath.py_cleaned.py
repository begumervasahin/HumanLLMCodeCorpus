class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(b11, k):
    if not b11:
        return
    b4 = []
    b5 = []
    b6 = b11
    while True:
        while b6:
            b4.append(b6)
            if b5:
                b7 = b5[-1] + b6.b1
            else:
                b7 = b6.b1
            b5.append(b7)
            b6 = b6.b2
        while b6 is None and b4:
            b6 = b4.pop()
            b7 = b5.pop()
            b8 = b7
            b9 = len(b5)
            for i in range(b9 - 1, -1, -1):
                if b8 = = k:
                    fonk3(b4, i + 1)
                b8 -= b4[i].b1
            b6 = b6.b3
        if b6 is None and not b4:
            break
def fonk3(b4, length):
    for i in range(len(b4) - length, len(b4)):
        print(b4[i].b1, b10 = " ")
    print()
b11 = class1(1)
b11.b2 = class1(3)
b11.b2.b2 = class1(2)
b11.b2.b3 = class1(1)
b11.b2.b3.b2 = class1(1)
b11.b3 = class1(-1)
b11.b3.b2 = class1(4)
b11.b3.b2.b2 = class1(1)
b11.b3.b2.b3 = class1(2)
b11.b3.b3 = class1(5)
b11.b3.b3.b3 = class1(6)
fonk2(b11, 5)