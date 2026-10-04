class class1:
    def fonk1(self, value):
        self.b1 = value
        self.b2 = None
        self.b3 = None
def fonk2(b6, b4 = None):
    if b4 is None:
        b4 = []
    if b6:
        fonk2(b6.b2, b4)
        if b6.b1 is not None:
            b4.append(b6.b1)
        fonk2(b6.b3, b4)
    return b4
def fonk3(b6, b4 = None):
    if b4 is None:
        b4 = []
    if b6:
        if b6.b1 is not None:
            b4.append(b6.b1)
        fonk3(b6.b2, b4)
        fonk3(b6.b3, b4)
    return b4
def fonk4(values, b5 = 0):
    if b5 < len(values) and values[b5] is not None:
        b6 = class1(values[b5])
        b6.b2 = fonk4(values, 2 * b5 + 1)
        b6.b3 = fonk4(values, 2 * b5 + 2)
        return b6
    return None
def fonk5(title, b4):
    print(title)
    for value in b4:
        print(value)
    print(" ")
b7 = [
    [1, None, 2, None, None, 3],
    [1, 2, 3, 4, 5, 6, None],
    [1, 2, 3]
]
for arr in b7:
    b8 = fonk4(arr)
    b9 = fonk2(b8)
    fonk5("In-order Traversal", b9)
    b10 = fonk3(b8)
    fonk5("Pre-order Traversal", b10)