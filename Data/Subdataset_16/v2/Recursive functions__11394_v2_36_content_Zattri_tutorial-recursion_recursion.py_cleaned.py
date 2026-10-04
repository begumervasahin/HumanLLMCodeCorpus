
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
    def fonk4(self, b3):
        self.b3 = b3
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
    if root.b4:
        print("Left")
        fonk7(root.b4)
    if root.b5:
        print("Right")
        fonk7(root.b5)
    if not (root.b4 or root.b5):
        print("Up")
def fonk8(root, val):
    if root.b3 = = val:
        print("Found")
    else:
        if root.b4:
            fonk8(root.b4, val)
        if root.b5:
            fonk8(root.b5, val)
def fonk9(arr):
    if len(arr) < 2:
        return arr
    b12 = len(arr)
    b13 = fonk9(arr[:b12])
    b14 = fonk9(arr[b12:])
    return fonk10(b13, b14)
def fonk10(b4, b5):
    b15 = []
    b16 = j = 0
    while b16 < len(b4) and j < len(b5):
        if b4[b16] > b5[j]:
            b15.append(b5[j])
            j += 1
        else:
            b15.append(b4[b16])
            b16 += 1
    b15.extend(b4[b16:])
    b15.extend(b5[j:])
    return b15
if b17 = = "__main__":
    print("Countdown from 5:")
    fonk1(5)
    print("Factorial of 5:", fonk2(5))
    print("Tail-recursive factorial of 5:", fonk3(5))
    print("Tree traversal:")
    fonk7(b6)
    print("Tree search for b3 4:")
    fonk8(b6, 4)
    b18 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("Sorted list:", fonk9(b18))