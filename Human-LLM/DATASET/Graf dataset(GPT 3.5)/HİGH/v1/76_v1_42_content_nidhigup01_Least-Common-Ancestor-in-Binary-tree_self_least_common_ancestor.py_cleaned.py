class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(T, b1, n1, n2):
    def fonk3(T, b1, parent):
        b4 = class1(b1)
        if not T or not T[b1]:
            return None
        for child in range(len(T[b1])):
            if T[b1][child] == 1 and child != parent:
                if child < b1:
                    b4.b2 = fonk3(T, child, b1)
                else:
                    b4.b3 = fonk3(T, child, b1)
        return b4
    b5 = fonk3(T, b1, -1)
    def fonk4(b4, n1, n2):
        if b4 is None:
            return None
        if b4.b1 = = n1 or b4.b1 == n2:
            return b4
        b6 = fonk4(b4.b2, n1, n2)
        b7 = fonk4(b4.b3, n1, n2)
        if b6 and b7:
            return b4
        return b6 if b6 is not None else b7
    b8 = fonk4(b5, n1, n2)
    return b8.b1 if b8 else None
print("LCA(1, 4) =", fonk2([[0, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [1, 0, 0, 0, 1],
                                [0, 0, 0, 0, 0]], b1 = 3, n1=1, n2=4))