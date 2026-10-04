from random import randint
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self, b1):
        if b1 < self.b1:
            if self.b2 is None:
                self.b2 = class1(b1)
            else:
                self.b2.fonk6(b1)
        elif b1 > self.b1:
            if self.b3 is None:
                self.b3 = class1(b1)
            else:
                self.b3.fonk6(b1)
    def fonk3(self):
        b4 = []
        self.fonk4(self, b4)
        return b4
    def fonk4(self, node, b4):
        if node:
            b4.append(node.b1)
            self.fonk4(node.b2, b4)
            self.fonk4(node.b3, b4)
class class2:
    def fonk5(self):
        self.b5 = None
    def fonk6(self, b1):
        if self.b5 is None:
            self.b5 = class1(b1)
        else:
            self.b5.fonk6(b1)
    def fonk7(self, b1):
        return self.fonk8(self.b5, b1)
    def fonk8(self, node, b1):
        if node is None:
            return False
        if b1 = = node.b1:
            return True
        if b1 < node.b1:
            return self.fonk8(node.b2, b1)
        return self.fonk8(node.b3, b1)
    def fonk9(self):
        if self.b5 is not None:
            return self.b5.fonk9()
        return []
    def fonk10(self):
        b6 = self.fonk9()
        b6.sort()
        b7 = len(b6)
        self.b5 = class1(b6.pop(b7))
        for b1 in b6:
            self.fonk6(b1)
        return self.fonk9()
b8 = class2()
for _ in range(50):
    b8.fonk6(randint(0, 100))
print("Original b8 (DFS b4):", b8.fonk9())
print("Rearranged b8 (DFS b4):", b8.fonk10())
print("Is 55 in the b8?", b8.fonk7(55))