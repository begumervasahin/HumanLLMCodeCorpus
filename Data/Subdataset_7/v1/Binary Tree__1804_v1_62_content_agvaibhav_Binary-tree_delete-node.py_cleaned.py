class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(b12):
    if b12 is None:
        return
    b4 = []
    b4.append(b12)
    while len(b4) > 0:
        print(b4[0].b1, b5 = ' ')
        b6 = b4.pop(0)
        if b6.b2 is not None:
            b4.append(b6.b2)
        if b6.b3 is not None:
            b4.append(b6.b3)
def fonk3(b12):
    if b12 is None:
        return
    fonk3(b12.b2)
    print(b12.b1, b5 = ' ')
    fonk3(b12.b3)
def fonk4(b12, b10):
    if b12 is None:
        return
    b7 = []
    b7.append(b12)
    while len(b7) > 0:
        b6 = b7.pop(0)
        if b6 = = b10:
            b6 = None
            return
        if b6.b3:
            if b6.b3 = = b10:
                b6.b3 = None
                return
            else:
                b7.append(b6.b3)
        if b6.b2:
            if b6.b2 = = b10:
                b6.b2 = None
                return
            else:
                b7.append(b6.b2)
def fonk5(b12, dele):
    if b12 is None:
        return
    b8 = []
    b8.append(b12)
    while len(b8) > 0:
        b6 = b8.pop(0)
        if b6.b1 = = dele:
            b9 = b6
        if b6.b2 is not None:
            b8.append(b6.b2)
        if b6.b3 is not None:
            b8.append(b6.b3)
    b10 = b6
    fonk4(b12, b10)
    b9.b1 = b10.b1
if b11 = = '__main__':
    b12 = class1(10)
    b12.b2 = class1(11)
    b12.b2.b2 = class1(7)
    b12.b2.b3 = class1(12)
    b12.b3 = class1(9)
    b12.b3.b2 = class1(15)
    b12.b3.b3 = class1(8)
    print("The tree before the deletion:")
    fonk3(b12)
    print()
    fonk2(b12)
    a1 = 11
    fonk5(b12, a1)
    print()
    print("The tree after the deletion:")
    fonk3(b12)
    print()
    fonk2(b12)