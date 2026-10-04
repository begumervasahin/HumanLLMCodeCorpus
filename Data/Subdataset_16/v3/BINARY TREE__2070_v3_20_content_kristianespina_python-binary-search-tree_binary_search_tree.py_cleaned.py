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
    def fonk3(self, array):
        if self.b2:
            self.b2.fonk8(array)
        array.append(self.b1)
        if self.b3:
            self.b3.fonk8(array)
        return array
class class2:
    def fonk4(self):
        self.b4 = None
    def fonk5(self, b5):
        if self.b4 is None:
            self.b4 = class1(b5)
        else:
            self.b4.fonk5(b5)
    def fonk6(self, b5):
        return self.fonk7(self.b4, b5)
    def fonk7(self, node, b5):
        if node is None:
            return False
        if b5 = = node.b1:
            return True
        elif b5 < node.b1:
            return self.fonk7(node.b2, b5)
        else:
            return self.fonk7(node.b3, b5)
    def fonk8(self):
        if self.b4:
            return self.b4.fonk8([])
        return []
    def fonk9(self):
        b6 = self.fonk8()
        b6.sort()
        b7 = len(b6)
        self.b4 = class1(b6.pop(b7))
        for element in b6:
            self.b4.fonk5(element)
        return self.fonk8()
b8 = class2()
for _ in range(50):
    b8.fonk5(randint(0, 100))
print("Original b8 (DFS):", b8.fonk8())
print("Rearranged b8 (DFS):", b8.fonk9())
print("Find 55:", b8.fonk6(55))