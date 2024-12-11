class class1:
    b1 = []
    def fonk1(self, b4):
        self.b1 = []
        if b4:
            for item in list(set(b4)):
                self.b1.append([item])
    def fonk2(self, elem):
        for item in self.b1:
            if elem in item:
                return self.b1.index(item)
        return None
    def fonk3(self, elem):
        for item in self.b1:
            if elem in item:
                return item
        return None
    def fonk4(self, elem1, elem2):
        b2 = self.fonk2(elem1)
        b3 = self.fonk2(elem2)
        if b2 != b3 and b2 is not None and b3 is not None:
            self.b1[b3] = self.b1[b3] + self.b1[b2]
            del self.b1[b2]
        return self.b1
    def fonk5(self):
        return self.b1
b4 = [1, 2, 3, 4, 5]
b5 = class1(b4)
print("Initial disjoint set:", b5.fonk5())
b5.fonk4(1, 2)
b5.fonk4(3, 4)
b5.fonk4(4, 5)
print("After unions:", b5.fonk5())
print("Find 1:", b5.fonk3(1))
print("Find 2:", b5.fonk3(2))
print("Find 3:", b5.fonk3(3))
print("Find 4:", b5.fonk3(4))
print("Find 5:", b5.fonk3(5))
print("Find 6:", b5.fonk3(6))