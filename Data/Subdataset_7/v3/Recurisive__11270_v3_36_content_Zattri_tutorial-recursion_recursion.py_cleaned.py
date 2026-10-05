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
def fonk7():
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
    return b6
def fonk8(root):
    print(root.b1)
    if root.b2:
        print("Left")
        fonk8(root.b2)
    if root.b3:
        print("Right")
        fonk8(root.b3)
def fonk9(root, val):
    if root is None:
        return
    if root.b1 = = val:
        print("Found")
    else:
        fonk9(root.b2, val)
        fonk9(root.b3, val)
def fonk10(b18):
    if len(b18) < 2:
        return b18
    b12 = len(b18)
    b13 = fonk10(b18[:b12])
    b14 = fonk10(b18[b12:])
    return fonk11(b13, b14)
def fonk11(b2, b3):
    b15 = []
    b16 = j = 0
    while b16 < len(b2) and j < len(b3):
        if b2[b16] < b3[j]:
            b15.append(b2[b16])
            b16 += 1
        else:
            b15.append(b3[j])
            j += 1
    b15.extend(b2[b16:])
    b15.extend(b3[j:])
    return b15
if b17 = = "__main__":
    fonk4(5)
    print(fonk5(5))
    print(fonk6(5))
    b6 = fonk7()
    fonk8(b6)
    fonk9(b6, 3)
    b18 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(fonk10(b18))