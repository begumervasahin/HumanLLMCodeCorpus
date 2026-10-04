
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(b5, b1, a2, a3):
    b4 = class1(b1)
    if b4 is None or b5 is None or b5 = = [[]]:
        return None
    b6 = len(b5[0])
    for child in range(b6):
        if b5[b1][child] == 1 and child < b1:
            b4.b2 = child
        elif b5[b1][child] == 1 and child > b1:
            b4.b3 = child
    if b4.b1 = = a2 or b4.b1 == a3:
        return b4
    b7 = None
    b8 = None
    if b4.b2 is not None:
        b7 = fonk2(b5, b4.b2, a2, a3)
    if b4.b3 is not None:
        b8 = fonk2(b5, b4.b3, a2, a3)
    if b7 and b8:
        return b4
    return b7 if b7 is not None else b8
def fonk3(b5, a1, a2, a3):
    b9 = fonk2(b5, a1, a2, a3)
    return b9.b1 if b9 else None
b5 = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
]
a1 = 3
a2 = 1
a3 = 4
print("LCA({}, {}) = {}".format(a2, a3, fonk3(b5, a1, a2, a3)))