class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(b5, b10, node1, node2):
    b4 = class1(b10)
    if b4 is None or b5 is None or b5 = = [[]]:
        return None
    b6 = len(b5)
    b7 = len(b5[0])
    for child in range(b7):
        if b5[b10][child] == 1 and child <= b10:
            b4.b2 = child
        elif b5[b10][child] == 1 and child > b10:
            b4.b3 = child
    if b4.b1 = = node1 or b4.b1 == node2:
        return b4
    b8 = fonk2(b5, b4.b2, node1, node2)
    b9 = fonk2(b5, b4.b3, node1, node2)
    if b8 and b9:
        return b4
    return b8 if b8 is not None else b9
print("LCA(4,5) = ", fonk2([[0, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [1, 0, 0, 0, 1],
                                [0, 0, 0, 0, 0]], b10 = 3, node1=1, node2=4))