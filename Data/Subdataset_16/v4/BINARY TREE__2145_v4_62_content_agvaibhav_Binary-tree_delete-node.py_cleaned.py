class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(b10):
    if not b10:
        return
    b4 = [b10]
    while b4:
        b5 = b4.pop(0)
        print(b5.b1, b6 = ' ')
        if b5.b2:
            b4.append(b5.b2)
        if b5.b3:
            b4.append(b5.b3)
def fonk3(b10):
    if not b10:
        return
    fonk3(b10.b2)
    print(b10.b1, b6 = ' ')
    fonk3(b10.b3)
def fonk4(b10, d_node):
    if not b10:
        return
    b4 = [b10]
    while b4:
        b5 = b4.pop(0)
        if b5 = = d_node:
            b5 = None
            return
        if b5.b3:
            if b5.b3 = = d_node:
                b5.b3 = None
                return
            else:
                b4.append(b5.b3)
        if b5.b2:
            if b5.b2 = = d_node:
                b5.b2 = None
                return
            else:
                b4.append(b5.b2)
def fonk5(b10, a1):
    if not b10:
        return
    if b10.b2 is None and b10.b3 is None:
        if b10.b1 = = a1:
            return None
        else:
            return b10
    b7 = None
    b4 = [b10]
    while b4:
        b5 = b4.pop(0)
        if b5.b1 = = a1:
            b7 = b5
        if b5.b2:
            b4.append(b5.b2)
        if b5.b3:
            b4.append(b5.b3)
    if b7:
        b8 = b5.b1
        fonk4(b10, b5)
        b7.b1 = b8
    return b10
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
    b10 = fonk5(b10, a1)
    print("The tree after the deletion:")
    fonk3(b10)
    print()
    fonk2(b10)
    print()