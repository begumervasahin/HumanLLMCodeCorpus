class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(b10, b8):
    if b8 is None:
        return None
    b4 = class1(b8)
    b5 = [i for i, val in enumerate(b10[b8]) if val == 1]
    if b5:
        if b5[0] < b8:
            b4.b2 = fonk2(b10, b5[0])
        if len(b5) > 1 and b5[1] > b8:
            b4.b3 = fonk2(b10, b5[1])
    return b4
def fonk3(b8, a2, a3):
    if b8 is None:
        return None
    if b8.b1 = = a2 or b8.b1 == a3:
        return b8
    b6 = fonk3(b8.b2, a2, a3)
    b7 = fonk3(b8.b3, a2, a3)
    if b6 and b7:
        return b8
    return b6 if b6 is not None else b7
def fonk4(b10, a1, a2, a3):
    b8 = fonk2(b10, a1)
    b9 = fonk3(b8, a2, a3)
    return b9.b1 if b9 else None
b10 = [[0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0]]
a1 = 3
a2 = 1
a3 = 4
print("LCA({}, {}) = {}".format(a2, a3, fonk4(b10, a1, a2, a3)))