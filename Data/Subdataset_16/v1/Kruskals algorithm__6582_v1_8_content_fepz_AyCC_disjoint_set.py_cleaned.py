class class1:
    def fonk1(self, b10):
        self.b1 = list(b10)
        self.b2 = list(range(len(b10)))
        self.b3 = [1] * len(b10)
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
        b7 = self.fonk2(self.b1[a])
        b8 = self.fonk2(self.b1[b])
        if b7 != b8:
            if self.b3[b7] > self.b3[b8]:
                self.b2[b8] = b7
            elif self.b3[b7] < self.b3[b8]:
                self.b2[b7] = b8
            else:
                self.b2[b8] = b7
                self.b3[b7] += 1
if b9 = = "__main__":
    b10 = ['A', 'B', 'C', 'D', 'E']
    b11 = class1(b10)
    print("Initial b2:")
    for e in b10:
        print(f"{e}: {b11.fonk2(e)}")
    b11.fonk3(0, 1)
    b11.fonk3(1, 2)
    print("\nSets after some merges:")
    for e in b10:
        print(f"{e}: {b11.fonk2(e)}")
    b11.fonk3(3, 4)
    b11.fonk3(2, 3)
    print("\nFinal b2 after all merges:")
    for e in b10:
        print(f"{e}: {b11.fonk2(e)}")