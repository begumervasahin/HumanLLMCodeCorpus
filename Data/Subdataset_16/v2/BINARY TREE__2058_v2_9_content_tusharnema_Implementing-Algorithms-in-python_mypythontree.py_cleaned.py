class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
        self.a1 = 1
def fonk2(b5):
    if b5:
        fonk2(b5.b2)
        print(b5.b1, b4 = ' ')
        fonk2(b5.b3)
def fonk3(b5):
    while b5 and b5.b3:
        b5 = b5.b3
    return b5
def fonk4(b5):
    while b5 and b5.b2:
        b5 = b5.b2
    return b5
def fonk5(b5, b1):
    if b5 is None:
        return class1(b1)
    elif b1 < b5.b1:
        b5.b2 = fonk5(b5.b2, b1)
    else:
        b5.b3 = fonk5(b5.b3, b1)
    return b5
def fonk6(b5, key):
    if b5 is None or b5.b1 = = key:
        return b5
    if key < b5.b1:
        return fonk6(b5.b2, key)
    return fonk6(b5.b3, key)
def fonk7(b5):
    if b5 is None:
        return 0
    return 1 + max(fonk7(b5.b2), fonk7(b5.b3))
def fonk8(b5, b1):
    if b5 is None:
        return None
    if b1 < b5.b1:
        b5.b2 = fonk8(b5.b2, b1)
    elif b1 > b5.b1:
        b5.b3 = fonk8(b5.b3, b1)
    else:
        if b5.b2 is None:
            return b5.b3
        if b5.b3 is None:
            return b5.b2
        b6 = fonk4(b5.b3)
        b5.b1 = b6.b1
        b5.b3 = fonk8(b5.b3, b6.b1)
    return b5
def fonk9(b5, x, b10):
    if b5 is None:
        return None
    if b5.b1 < x and b5.b1 < b10:
        return fonk9(b5.b3, x, b10)
    if b5.b1 > x and b5.b1 > b10:
        return fonk9(b5.b2, x, b10)
    return b5
def fonk10(arr):
    if not arr:
        return None
    b7 = len(arr)
    b5 = class1(arr[b7])
    b5.b2 = fonk10(arr[:b7])
    b5.b3 = fonk10(arr[b7 + 1:])
    return b5
if b8 = = '__main__':
    b5 = None
    b9 = [6, 7, -2, 4, 1, 9, 11, 5]
    for node in b9:
        b5 = fonk5(b5, node)
    print("In-order traversal of the BST:")
    fonk2(b5)
    print()
    x, b10 = 1, 5
    b11 = fonk9(b5, x, b10)
    if b11:
        print(f"The lowest common b11 of {x} and {b10} is: {b11.b1}")
    else:
        print(f"There is no common b11 for {x} and {b10}")