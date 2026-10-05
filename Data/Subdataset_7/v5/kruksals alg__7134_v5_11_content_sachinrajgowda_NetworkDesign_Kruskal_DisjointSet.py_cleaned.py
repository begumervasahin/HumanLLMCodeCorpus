class class1(dict):
    def fonk1(self, item):
        self[item] = item
    def fonk2(self, item):
        b1 = self[item]
        while self[b1] != b1:
            b1 = self[b1]
        self[item] = b1
        return b1
    def fonk3(self, item1, item2):
        self[item2] = self[item1]
def fonk4(b8, b10):
    b2 = class1()
    b3 = []
    for node in b8:
        b2.fonk1(node)
    b4 = len(b8) - 1
    for edge in b10:
        src, dest, b5 = edge
        b6 = b2.fonk2(src)
        b7 = b2.fonk2(dest)
        if b6 != b7:
            b3.append(edge)
            b4 -= 1
            if b4 = = 0:
                return b3
            b2.fonk3(b6, b7)
b8 = [1, 2, 3, 4]
b9 = [(1, 2, 1), (1, 3, 2), (2, 3, 3), (2, 4, 4), (3, 4, 5)]
b10 = sorted(b9, key=lambda x: x[2])
b11 = fonk4(b8, b10)
print(b11)