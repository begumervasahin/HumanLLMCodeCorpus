class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
        self.a1 = 1
def fonk2(b6):
    if b6:
        fonk2(b6.b2)
        print(b6.b1, b4 = ' ')
        fonk2(b6.b3)
def fonk3(b6):
    b5 = None
    while b6:
        b5 = b6
        b6 = b6.b3
    return b5
def fonk4(b6, b1):
    if b6 is None:
        b6 = class1(b1)
    elif b6.b1 > b1:
        b6.b2 = fonk4(b6.b2, b1)
    else:
        b6.b3 = fonk4(b6.b3, b1)
    return b6
def fonk5(b6, key):
    if b6 is None or b6.b1 = = key:
        return b6
    else:
        if b6.b1 > key:
            return fonk5(b6.b2, key)
        else:
            return fonk5(b6.b3, key)
def fonk6(b6):
    b5 = None
    while b6:
        b5 = b6
        b6 = b6.b2
    return b5
def fonk7(b6):
    if b6:
        return 1 + max(fonk7(b6.b2), fonk7(b6.b3))
    return 0
def fonk8(b6, b1):
    if b6 is None:
        return None
    if b6.b1 < b1:
        b6.b3 = fonk8(b6.b3, b1)
    elif b6.b1 > b1:
        b6.b2 = fonk8(b6.b2, b1)
    else:
        if b6.b2 is None:
            return b6.b3
        if b6.b3 is None:
            return b6.b2
        b7 = fonk6(b6.b3)
        b6.b1 = b7.b1
        b6.b3 = fonk8(b6.b3, b7.b1)
    return b6
def fonk9(b6, key1, b8):
    if key1 > b8:
        key1, b8 = b8, key1
    if b6 is None:
        return None
    if b6.b1 >= key1 and b6.b1 <= b8:
        return b6
    else:
        if b6.b1 > key1 and b6.b1 > b8:
            return fonk9(b6.b2, key1, b8)
        else:
            return fonk9(b6.b3, key1, b8)
def fonk10(arr):
    if not arr:
        return None
    b9 = len(arr)
    b6 = class1(arr[b9])
    b6.b2 = fonk10(arr[:b9])
    b6.b3 = fonk10(arr[b9+1:])
    return b6
def fonk11(b6, x, y):
    if b6 is None:
        return None
    if (b6.b1 < x and b6.b1 < y):
        return fonk11(b6.b3, x, y)
    if (b6.b1 > x and b6.b1 > y):
        return fonk11(b6.b2, x, y)
    return b6
b6 = None
b6 = fonk4(b6, 6)
b6 = fonk4(b6, 7)
b6 = fonk4(b6, -2)
b6 = fonk4(b6, 4)
b6 = fonk4(b6, 1)
b6 = fonk4(b6, 9)
b6 = fonk4(b6, 11)
b6 = fonk4(b6, 5)
print("In-order Traversal:")
fonk2(b6)
print()
print("Lowest Common Ancestor of 1 and 5:", fonk11(b6, 1, 5).b1)