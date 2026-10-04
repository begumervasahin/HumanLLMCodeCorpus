
def fonk1(b1):
    print(b1)
    if b1 > 0:
        fonk1(b1 - 1)
def fonk2(b1):
    if b1 = = 0:
        return 1
    else:
        return b1 * fonk2(b1 - 1)
def fonk3(b1, b2 = 1):
    if b1 = = 0:
        return b2
    else:
        return fonk3(b1 - 1, b2 * b1)
class class1:
    def fonk4(self, value):
        self.b3 = value
        self.b4 = None
        self.b5 = None
    def fonk5(self, node):
        self.b4 = node
    def fonk6(self, node):
        self.b5 = node
b6 = class1(0)
b7 = class1(1)
b8 = class1(2)
b9 = class1(3)
b10 = class1(4)
b11 = class1(5)
b6.fonk5(b7)
b6.fonk6(b8)
b7.fonk5(b9)
b8.fonk5(b10)
b8.fonk6(b11)
def fonk7(root):
    print(root.b3)
    if root.b4 or root.b5:
        if root.b4:
            print("Left")
            fonk7(root.b4)
        if root.b5:
            print("Right")
            fonk7(root.b5)
    else:
        print("Up")
def fonk8(root, val):
    if root.b3 = = val:
        print("Found")
    else:
        if root.b4 or root.b5:
            if root.b4:
                fonk8(root.b4, val)
            if root.b5:
                fonk8(root.b5, val)
def fonk9(b1):
    b12 = []
    if len(b1) < 2:
        return b1
    b13 = len(b1)
    b14 = fonk9(b1[:b13])
    b15 = fonk9(b1[b13:])
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
    fonk1(5)
    print("Factorial of 5:", fonk2(5))
    print("Tail-recursive factorial of 5:", fonk3(5))
    print("Tree traversal:")
    fonk7(b6)
    print("Tree search for value 4:")
    fonk8(b6, 4)
    b17 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("Sorted list:", fonk9(b17))