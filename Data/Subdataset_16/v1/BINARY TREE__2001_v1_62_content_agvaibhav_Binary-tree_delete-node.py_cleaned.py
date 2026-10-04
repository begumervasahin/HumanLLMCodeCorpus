class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(b10):
    if b10 is None:
        return
    b4 = []
    b4.append(b10)
    while len(b4) > 0:
        print(b4[0].b1, b5 = ' ')
        b6 = b4.pop(0)
        if b6.b2 is not None:
            b4.append(b6.b2)
        if b6.b3 is not None:
            b4.append(b6.b3)
def fonk3(b10):
    if b10 is None:
        return
    fonk3(b10.b2)
    print(b10.b1, b5 = ' ')
    fonk3(b10.b3)
def fonk4(b10, b8):
    if b10 is None:
        return
    b4 = []
    b4.append(b10)
    while len(b4) > 0:
        b6 = b4.pop(0)
        if b6 = = b8:
            b6 = None
            return
        if b6.b3:
            if b6.b3 = = b8:
                b6.b3 = None
                return
            else:
                b4.append(b6.b3)
        if b6.b2:
            if b6.b2 = = b8:
                b6.b2 = None
                return
            else:
                b4.append(b6.b2)
def fonk5(b10, a1):
    if b10 is None:
        return
    b4 = []
    b4.append(b10)
    b7 = None
    while len(b4) > 0:
        b6 = b4.pop(0)
        if b6.b1 = = a1:
            b7 = b6
        if b6.b2 is not None:
            b4.append(b6.b2)
        if b6.b3 is not None:
            b4.append(b6.b3)
    if b7:
        b8 = b6
        fonk4(b10, b8)
        b7.b1 = b8.b1
if b9 = = '__main__':
    b10 = class1(10)
    b10.b2 = class1(11)
    b10.b2.b2 = class1(7)
    b10.b2.b3 = class1(12)
    b10.b3 = class1(9)
    b10.b3.b2 = class1(15)
    b10.b3.b3 = class1(8)
    print("The tree before the deletion:")
    fonk3(b10)
    print()
    fonk2(b10)
    print()
    a1 = 11
    fonk5(b10, a1)
    print("The tree after the deletion:")
    fonk3(b10)
    print()
    fonk2(b10)
    print()