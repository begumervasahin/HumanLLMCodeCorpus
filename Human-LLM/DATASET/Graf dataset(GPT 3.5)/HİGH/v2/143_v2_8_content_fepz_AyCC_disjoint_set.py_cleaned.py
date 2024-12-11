class class1:
    def fonk1(self, b1):
        self.b1 = list(b1)
        self.b2 = list(range(len(b1)))
        self.b3 = [1] * len(b1)
    def fonk2(self, x):
        b4 = b5 = self.b1.index(x)
        while self.b2[b5] != b5:
            b5 = self.b2[b5]
        while b4 != b5:
            b6 = self.b2[b4]
            self.b2[b4] = b5
            b4 = b6
        return b5
    def fonk3(self, a, b):
        if self.b3[a] == self.b3[b]:
            self.b3[a] += 1
            self.b2[b] = a
        else:
            if self.b3[a] > self.b3[b]:
                self.b2[b] = a
            else:
                self.b2[a] = b
b1 = ['A', 'B', 'C', 'D', 'E']
b7 = class1(b1)
print("Initial sets:", b7.b2)
print("Initial b3:", b7.b3)
b7.fonk3(b7.fonk2('A'), b7.fonk2('B'))
print("\nAfter merging sets containing 'A' and 'B':")
print("Sets:", b7.b2)
print("Ranks:", b7.b3)
b7.fonk3(b7.fonk2('C'), b7.fonk2('D'))
print("\nAfter merging sets containing 'C' and 'D':")
print("Sets:", b7.b2)
print("Ranks:", b7.b3)