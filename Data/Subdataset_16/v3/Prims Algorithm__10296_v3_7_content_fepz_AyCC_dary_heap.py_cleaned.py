import math
class class1:
    def fonk1(self, b1, b3):
        self.b1 = b1
        self.b2 = None
        self.b3 = b3
class class2:
    def fonk2(self, b4 = 2):
        self.b5 = []
        self.b4 = b4
    def fonk3(self, node, b2):
        while True:
            b6 = self.fonk11(b2)
            if b6 is None or self.b5[b6].b1 >= node.b1:
                break
            self.b5[b2] = self.b5[b6]
            self.b5[b2].b2 = b2
            b2 = b6
        self.b5[b2] = node
        node.b2 = b2
    def fonk4(self, node, b2):
        while b2 > 0:
            b7 = self.fonk9(b2)
            if self.b5[b7].b1 <= node.b1:
                break
            self.b5[b2] = self.b5[b7]
            self.b5[b2].b2 = b2
            b2 = b7
        self.b5[b2] = node
        node.b2 = b2
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
    def fonk7(self, b1, b3):
        b10 = class1(b1, b3)
        self.b5.append(b10)
        self.fonk4(b10, len(self.b5) - 1)
        return b10
    def fonk8(self, node, newkey):
        node.b1 = newkey
        self.fonk4(node, node.b2)
    def fonk9(self, b2):
        if b2 = = 0:
            return None
        return (b2 - 1)
    def fonk10(self, b2):
        return range(self.b4 * b2 + 1, min(self.b4 * (b2 + 1) + 1, len(self.b5)))
    def fonk11(self, b2):
        b11 = None
        b12 = None
        for b6 in self.fonk10(b2):
            if b12 is None or self.b5[b6].b1 < b12:
                b12 = self.b5[b6].b1
                b11 = b6
        return b11
if b13 = = "__main__":
    b5 = class2(b4=3)
    b5.fonk7(5, "A")
    b5.fonk7(3, "B")
    b5.fonk7(8, "C")
    b5.fonk7(1, "D")
    print("Minimum:", b5.fonk5().b1)
    b5.fonk6()
    print("New Minimum:", b5.fonk5().b1)
