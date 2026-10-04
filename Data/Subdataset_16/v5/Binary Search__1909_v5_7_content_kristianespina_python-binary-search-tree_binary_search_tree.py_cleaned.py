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
                self.b2.fonk5(b1)
        elif b1 > self.b1:
            if self.b3 is None:
                self.b3 = class1(b1)
            else:
                self.b3.fonk5(b1)
    def fonk3(self, node, array):
        if node:
            array.append(node.b1)
            self.fonk8(node.b2, array)
            self.fonk8(node.b3, array)
        return array
class class2:
    def fonk4(self):
        self.b4 = None
    def fonk5(self, b1):
        if self.b4 is None:
            self.b4 = class1(b1)
        else:
            self.b4.fonk5(b1)
    def fonk6(self, b1):
        return self.fonk7(self.b4, b1)
    def fonk7(self, node, b1):
        if node is None:
            return False
        if b1 = = node.b1:
            return True
        elif b1 < node.b1:
            return self.fonk7(node.b2, b1)
        else:
            return self.fonk7(node.b3, b1)
    def fonk8(self):
        if self.b4 is None:
            return []
        return self.b4.fonk8(self.b4, [])
    def fonk9(self):
        b5 = self.fonk8()
        b5.sort()
        b6 = len(b5)
        self.b4 = class1(b5.pop(b6))
        for b1 in b5:
            self.fonk5(b1)
        return self.fonk8()
if b7 = = "__main__":
    b8 = class2()
    for _ in range(50):
        b8.fonk5(randint(0, 100))
    print("Original Tree (DFS array form):", b8.fonk8())
    print("Rearranged Tree (Median as b4):", b8.fonk9())
    print("Finding 55 in the b8:", b8.fonk6(55))