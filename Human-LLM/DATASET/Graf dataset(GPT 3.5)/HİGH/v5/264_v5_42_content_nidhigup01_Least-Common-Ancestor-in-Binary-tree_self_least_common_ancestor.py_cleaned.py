class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(b4, b10, node1, node2):
    if b4 is None or b4 = = [[]]:
        return None
    b5 = class1(b10)
    b6 = len(b4)
    b7 = len(b4[0])
    for child in range(b7):
        if b4[b10][child] == 1 and child <= b10:
            b5.b2 = child
        elif b4[b10][child] == 1 and child > b10:
            b5.b3 = child
    if b5.b1 = = node1 or b5.b1 == node2:
        return b5
    b8 = fonk2(b4, b5.b2, node1, node2)
    b9 = fonk2(b4, b5.b3, node1, node2)
    if b8 and b9:
        return b5
    return b8 if b8 is not None else b9
print("LCA(4,5) = ", fonk2([[0, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [1, 0, 0, 0, 1],
                                [0, 0, 0, 0, 0]], b10 = 3, node1=1, node2=4))