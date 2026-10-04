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
    def fonk3(self, b4 = None):
        if b4 is None:
            b4 = []
        b4.append(self.b1)
        if self.b2:
            self.b2.fonk8(b4)
        if self.b3:
            self.b3.fonk8(b4)
        return b4
class class2:
    def fonk4(self):
        self.b5 = None
    def fonk5(self, b6):
        if self.b5 is None:
            self.b5 = class1(b6)
        else:
            self.b5.fonk5(b6)
    def fonk6(self, b6):
        return self.fonk7(self.b5, b6)
    def fonk7(self, node, b6):
        if node is None:
            return False
        if b6 = = node.b1:
            return True
        elif b6 < node.b1:
            return self.fonk7(node.b2, b6)
        else:
            return self.fonk7(node.b3, b6)
    def fonk8(self):
        if self.b5:
            return self.b5.fonk8()
        return []
    def fonk9(self):
        b7 = self.fonk8()
        b7.sort()
        b8 = len(b7)
        self.b5 = class1(b7.pop(b8))
        for b1 in b7:
            self.b5.fonk5(b1)
        return self.fonk8()
if b9 = = "__main__":
    b10 = class2()
    for _ in range(50):
        b10.fonk5(randint(0, 100))
    print("Tree in DFS Array Form:")
    print(b10.fonk8())
    print("\nRe-arranged Tree with Median as Root:")
    print(b10.fonk9())
    a1 = 55
    print(f"\nSearching for {a1} in the b10:")
    print("Found!" if b10.fonk6(a1) else "Not Found!")