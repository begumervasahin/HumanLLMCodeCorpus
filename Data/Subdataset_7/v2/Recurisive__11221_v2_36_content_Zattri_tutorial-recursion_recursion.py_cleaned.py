class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self, node):
        self.b2 = node
    def fonk3(self, node):
        self.b3 = node
def fonk4(b4):
    print(b4)
    if b4 > 0:
        fonk4(b4 - 1)
def fonk5(b4):
    if b4 = = 0:
        return 1
    else:
        return b4 * fonk5(b4 - 1)
def fonk6(b4, b5 = 1):
    if b4 = = 0:
        return b5
    else:
        return fonk6(b4 - 1, b5 * b4)
b6 = class1(0)
b7 = class1(1)
b8 = class1(2)
b9 = class1(3)
b10 = class1(4)
b11 = class1(5)
b6.fonk2(b7)
b6.fonk3(b8)
b7.fonk2(b9)
b8.fonk2(b10)
b8.fonk3(b11)
def fonk7(root):
    print(root.b1)
    if root.b2:
        print("Left")
        fonk7(root.b2)
    if root.b3:
        print("Right")
        fonk7(root.b3)
def fonk8(root, val):
    if root.b1 = = val:
        print("Found")
    elif root.b2:
        fonk8(root.b2, val)
    elif root.b3:
        fonk8(root.b3, val)
def fonk9(b4):
    b12 = []
    if len(b4) < 2:
        return b4
    b13 = len(b4)
    b14 = fonk9(b4[:b13])
    b15 = fonk9(b4[b13:])
    a1 = 0
    a2 = 0
    while a1 < len(b14) and a2 < len(b15):
        if b14[a1] > b15[a2]:
            b12.append(b15[a2])
            a2 += 1
        else:
            b12.append(b14[a1])
            a1 += 1
    b12 += b14[a1:]
    b12 += b15[a2:]
    return b12
if b16 = = "__main__":
    fonk4(5)
    print(fonk5(5))
    print(fonk6(5))
    fonk7(b6)
    fonk8(b6, 3)
    print(fonk9([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))