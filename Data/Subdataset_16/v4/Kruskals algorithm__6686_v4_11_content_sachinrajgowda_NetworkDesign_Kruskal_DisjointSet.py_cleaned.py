class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, b3):
        self.b1[b3] = b3
    def fonk3(self, b3):
        b2 = b3
        while self.b1[b2] != b2:
            b2 = self.b1[b2]
        while b3 != b2:
            b1 = self.b1[b3]
            self.b1[b3] = b2
            b3 = b1
        return b2
    def fonk4(self, item1, item2):
        b4 = self.fonk3(item1)
        b5 = self.fonk3(item2)
        if b4 != b5:
            self.b1[b5] = b4
def fonk5(nodes, sorted_edges):
    b6 = class1()
    b7 = []
    for node in nodes:
        b6.fonk2(node)
    b8 = len(nodes) - 1
    for edge in sorted_edges:
        src, dest, b9 = edge
        b10 = b6.fonk3(src)
        b11 = b6.fonk3(dest)
        if b10 != b11:
            b7.append(edge)
            b6.fonk4(src, dest)
            b8 -= 1
            if b8 = = 0:
                break
    return b7