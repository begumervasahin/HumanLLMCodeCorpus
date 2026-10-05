
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(b5, b1, n1, n2):
    b4 = class1(b1)
    print ('b4.b1', b4.b1)
    if b4 is None or b5 = = None or b5 == [[]]:
        return None
    b6 = len(b5)
    print ('b6', b6)
    b7 = len(b5[0])
    print ('b7', b7)
    b8 = b1
    print ('b8', b8)
    for child in range(0, b7):
        if b5[b8][child] == 1 and  child <= b8:
            b4.b2 = child
            print ('b4.b2', b4.b2 )
        elif b5[b8][child] == 0:
                pass
        elif b5[b8][child] == 1 and  child > b8:
            b4.b3 = child
            print ('b4.b3', b4.b3 )
    if b4.b1 = = n1 or b4.b1 == n2:
        return b4
    b9 = fonk2(b5, b4.b2, n1, n2)
    b10 = fonk2(b5, b4.b3, n1, n2)
    if b9 and b10:
        return b4
    return b9 if b9 is not None else b10
print ("LCA(4,5) = ", fonk2([[0, 1, 0, 0, 0],[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]], b1 = 3, n1 = 1, n2 = 4))