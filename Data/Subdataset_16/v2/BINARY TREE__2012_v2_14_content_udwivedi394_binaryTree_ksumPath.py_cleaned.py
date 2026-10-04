class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(b9, k):
    b4 = []
    b5 = []
    b6 = b9
    while True:
        while b6:
            b4.append(b6)
            if not b5:
                b5.append(b6)
                a1 = 0
            else:
                a1 = b5.pop()
                b5.append(b6)
            b5.append(b6.b1 + a1)
            b6 = b6.b2
        while b6 is None and b4:
            b6 = b4.pop()
            a1 = b5.pop()
            while b5 and b5[-1] != b6:
                a1 -= b5.pop().b1
            b7 = a1
            a2 = 0
            while a2 < len(b5):
                if b7 = = k:
                    for j in range(a2, len(b5)):
                        print(b5[j].b1, b8 = " ")
                    print()
                b7 -= b5[a2].b1
                a2 += 1
            b5.append(a1)
            b6 = b6.b3
        if b6 is None and not b4:
            break
b9 = class1(1)
b9.b2 = class1(3)
b9.b2.b2 = class1(2)
b9.b2.b3 = class1(1)
b9.b2.b3.b2 = class1(1)
b9.b3 = class1(-1)
b9.b3.b2 = class1(4)
b9.b3.b2.b2 = class1(1)
b9.b3.b2.b3 = class1(2)
b9.b3.b3 = class1(5)
b9.b3.b3.b3 = class1(6)
fonk2(b9, 5)