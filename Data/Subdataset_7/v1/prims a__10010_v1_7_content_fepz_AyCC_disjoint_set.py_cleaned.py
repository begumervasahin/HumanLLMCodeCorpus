class class1:
    def fonk1(self, b7):
        self.b1 = list(b7)
        self.b2 = list(range(len(b7)))
        self.b3 = [1] * len(b7)
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
            self.b3[a] = self.b3[a] + 1
            self.b2[b] = a
        else:
            if self.b3[a] > self.b3[b]:
                self.b2[b] = a
            else:
                self.b2[a] = b
b7 = ['A', 'B', 'C', 'D', 'E']
b8 = class1(b7)
print("Initial b2:", b8.b2)
print("Find 'A':", b8.fonk2('A'))
b8.fonk3(0, 1)
print("Sets after merging 'A' and 'B':", b8.b2)
print("Find 'B':", b8.fonk2('B'))
b8.fonk3(2, 3)
print("Sets after merging 'C' and 'D':", b8.b2)
print("Find 'D':", b8.fonk2('D'))