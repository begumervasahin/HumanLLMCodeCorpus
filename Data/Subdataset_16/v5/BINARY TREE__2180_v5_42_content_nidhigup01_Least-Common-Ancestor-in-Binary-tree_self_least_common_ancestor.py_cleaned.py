class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(b10, root_key):
    b4 = class1(root_key)
    b5 = {root_key: b4}
    for i, row in enumerate(b10):
        for j, b6 in enumerate(row):
            if b6 = = 1:
                if j not in b5:
                    b5[j] = class1(j)
                if j < i:
                    b5[i].b2 = b5[j]
                else:
                    b5[i].b3 = b5[j]
    return b4
def fonk3(b4, a2, a3):
    if b4 is None:
        return None
    if b4.b1 = = a2 or b4.b1 == a3:
        return b4
    b7 = fonk3(b4.b2, a2, a3)
    b8 = fonk3(b4.b3, a2, a3)
    if b7 and b8:
        return b4
    return b7 if b7 is not None else b8
def fonk4(b10, a1, a2, a3):
    b4 = fonk2(b10, a1)
    b9 = fonk3(b4, a2, a3)
    return b9.b1 if b9 else None
b10 = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
]
a1 = 3
a2 = 1
a3 = 4
print("LCA({}, {}) = {}".format(a2, a3, fonk4(b10, a1, a2, a3)))