import math
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = None
class class2:
    def fonk2(self, b4 = 2):
        self.b5 = []
        self.b4 = b4
    def fonk3(self, node, b3):
        b6 = self.fonk11(b3)
        while b6 is not None and self.b5[b6].b1 < node.b1:
            self.b5[b3] = self.b5[b6]
            self.b5[b3].b3 = b3
            b3 = b6
            b6 = self.fonk11(b3)
        self.b5[b3] = node
        node.b3 = b3
    def fonk4(self, node, b3):
        b7 = self.fonk9(b3)
        while b7 is not None and self.b5[b7].b1 > node.b1:
            self.b5[b3] = self.b5[b7]
            self.b5[b3].b3 = b3
            b3 = b7
            b7 = self.fonk9(b3)
        self.b5[b3] = node
        node.b3 = b3
    def fonk5(self):
        return self.b5[0] if self.b5 else None
    def fonk6(self):
        if not self.b5:
            return None
        b8 = self.b5[0]
        b9 = self.b5.pop()
        if self.b5:
            self.fonk3(b9, 0)
        return b8
    def fonk7(self, b1, b2):
        b10 = class1(b1, b2)
        self.b5.append(b10)
        self.fonk4(b10, len(self.b5) - 1)
        return b10
    def fonk8(self, node, newkey):
        node.b1 = newkey
        self.fonk4(node, node.b3)
    def fonk9(self, b3):
        if b3 = = 0:
            return None
        return (b3 - 1)
    def fonk10(self, b3):
        b11 = self.b4 * b3 + 1
        b12 = min(self.b4 * (b3 + 1) + 1, len(self.b5))
        return range(b11, b12)
    def fonk11(self, b3):
        b13 = None
        b14 = None
        for b6 in self.fonk10(b3):
            if b14 is None or self.b5[b6].b1 < b14:
                b14 = self.b5[b6].b1
                b13 = b6
        return b13