class class1(object):
    def fonk1(self, x):
        self.b15 = x
        self.b20 = None
        self.b3 = None
def fonk2(b9, root):
    if root:
        fonk2(b9, root.b20)
        if root.b15 is not None:
            b9.append(root.b15)
        fonk2(b9, root.b3)
    return b9
def fonk3(b9, root):
    if root:
        if root.b15 is not None:
            b9.append(root.b15)
        fonk3(b9, root.b20)
        fonk3(b9, root.b3)
        return b9
def fonk4(arr1, b5, i, b7):
    if i < b7:
        b4 = class1(arr1[i])
        b5 = b4
        b5.b20 = fonk4(arr1, b5.b20, 2 * i + 1, b7)
        b5.b3 = fonk4(arr1, b5.b3, 2 * i + 2, b7)
    return b5
b6 = [1, None, 2, None, None, 3]
b7 = len(b6)
b8 = None
b8 = fonk4(b6, b8, 0, b7)
b9 = []
b9 = fonk2(b9, b8)
print("In order Traversal")
for x in b9:
    print(x)
print(" ")
b10 = []
b10 = fonk3(b10, b8)
print("Pre-order Traversal")
for x in b10:
    print(x)
print(" ")
b11 = [1, 2, 3, 4, 5, 6, None]
b12 = len(b11)
b13 = None
b13 = fonk4(b11, b13, 0, b12)
b14 = []
b14 = fonk2(b14, b13)
print("In Order Traversal")
for x in b14:
    print(x)
print(" ")
b15 = []
b15 = fonk3(b15, b13)
print("Pre-order Traversal")
for x in b15:
    print(x)
b16 = [1, 2, 3]
b17 = len(b16)
b18 = None
b18 = fonk4(b16, b18, 0, b17)
b19 = []
b19 = fonk2(b19, b18)
print("In Order Traversal")
for x in b19:
    print(x)
print(" ")
b20 = []
b20 = fonk3(b20, b18)
print("Pre-order Traversal")
for x in b20:
    print(x)