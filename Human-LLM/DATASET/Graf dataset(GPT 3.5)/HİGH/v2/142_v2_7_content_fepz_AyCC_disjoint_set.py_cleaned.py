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
print("Initial b2:", b7.b2)
print("Find 'A':", b7.fonk2('A'))
b7.fonk3(0, 1)
print("Sets after merging 'A' and 'B':", b7.b2)
print("Find 'B':", b7.fonk2('B'))
b7.fonk3(2, 3)
print("Sets after merging 'C' and 'D':", b7.b2)
print("Find 'D':", b7.fonk2('D'))