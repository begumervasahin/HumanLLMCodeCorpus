class class1:
    def fonk1(self, x):
        self.b1 = x
        self.b2 = None
        self.b3 = None
def fonk2(b5, b4 = None):
    if b4 is None:
        b4 = []
    if b5:
        fonk2(b5.b2, b4)
        if b5.b1 is not None:
            b4.append(b5.b1)
        fonk2(b5.b3, b4)
    return b4
def fonk3(b5, b4 = None):
    if b4 is None:
        b4 = []
    if b5:
        if b5.b1 is not None:
            b4.append(b5.b1)
        fonk3(b5.b2, b4)
        fonk3(b5.b3, b4)
    return b4
def fonk4(arr, i, b7):
    b5 = None
    if i < b7:
        if arr[i] is not None:
            b5 = class1(arr[i])
            b5.b2 = fonk4(arr, 2 * i + 1, b7)
            b5.b3 = fonk4(arr, 2 * i + 2, b7)
    return b5
b6 = [1, None, 2, None, None, 3]
b7 = len(b6)
b8 = fonk4(b6, 0, b7)
print("In-order Traversal")
for x in fonk2(b8):
    print(x)
print()
print("Pre-order Traversal")
for x in fonk3(b8):
    print(x)
print()
b9 = [1, 2, 3, 4, 5, 6, None]
b10 = len(b9)
b11 = fonk4(b9, 0, b10)
print("In-order Traversal")
for x in fonk2(b11):
    print(x)
print()
print("Pre-order Traversal")
for x in fonk3(b11):
    print(x)
b12 = [1, 2, 3]
b13 = len(b12)
b14 = fonk4(b12, 0, b13)
print("In-order Traversal")
for x in fonk2(b14):
    print(x)
print()
print("Pre-order Traversal")
for x in fonk3(b14):
    print(x)