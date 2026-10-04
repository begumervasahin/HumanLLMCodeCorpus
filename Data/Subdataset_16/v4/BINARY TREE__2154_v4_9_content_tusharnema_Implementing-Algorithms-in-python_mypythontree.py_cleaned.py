class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(b7):
    if b7:
        fonk2(b7.b2)
        print(b7.b1, b4 = ' ')
        fonk2(b7.b3)
def fonk3(b7):
    b5 = b7
    while b5 and b5.b3:
        b5 = b5.b3
    return b5
def fonk4(b7, b1):
    if b7 is None:
        return class1(b1)
    if b1 < b7.b1:
        b7.b2 = fonk4(b7.b2, b1)
    else:
        b7.b3 = fonk4(b7.b3, b1)
    return b7
def fonk5(b7, key):
    if b7 is None or b7.b1 = = key:
        return b7
    if key < b7.b1:
        return fonk5(b7.b2, key)
    return fonk5(b7.b3, key)
def fonk6(b7):
    b5 = b7
    while b5 and b5.b2:
        b5 = b5.b2
    return b5
def fonk7(b7):
    if b7 is None:
        return 0
    return 1 + max(fonk7(b7.b2), fonk7(b7.b3))
def fonk8(b7, b1):
    if b7 is None:
        return b7
    if b1 < b7.b1:
        b7.b2 = fonk8(b7.b2, b1)
    elif b1 > b7.b1:
        b7.b3 = fonk8(b7.b3, b1)
    else:
        if b7.b2 is None:
            return b7.b3
        if b7.b3 is None:
            return b7.b2
        b6 = fonk6(b7.b3)
        b7.b1 = b6.b1
        b7.b3 = fonk8(b7.b3, b6.b1)
    return b7
def fonk9(b7, x, y):
    while b7:
        if b7.b1 < x and b7.b1 < y:
            b7 = b7.b3
        elif b7.b1 > x and b7.b1 > y:
            b7 = b7.b2
        else:
            break
    return b7
def fonk10(arr):
    if not arr:
        return None
    b8 = len(arr)
    b7 = class1(arr[b8])
    b7.b2 = fonk10(arr[:b8])
    b7.b3 = fonk10(arr[b8+1:])
    return b7
b7 = None
b7 = fonk4(b7, 6)
b7 = fonk4(b7, 7)
b7 = fonk4(b7, -2)
b7 = fonk4(b7, 4)
b7 = fonk4(b7, 1)
b7 = fonk4(b7, 9)
b7 = fonk4(b7, 11)
b7 = fonk4(b7, 5)
fonk2(b7)
print()
print("LCA of 1 and 5:", fonk9(b7, 1, 5).b1)