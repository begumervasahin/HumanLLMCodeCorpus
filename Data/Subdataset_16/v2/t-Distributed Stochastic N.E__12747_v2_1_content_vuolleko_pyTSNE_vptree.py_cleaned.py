import numpy as np
class class1:
    def fonk1(self, b15, data):
        if len(b15) == 0:
            self.b1 = None
            self.b2 = None
            self.b3 = None
            self.b4 = None
            return
        self.b1 = b15[0]
        b5 = b15[1:]
        if len(b5) > 0:
            b6 = np.sum((data[b5] - data[self.b1]) ** 2, axis=1)
            self.b2 = np.median(b6)
            b7 = b6 < self.b2
            b8 = ~b7
            self.b3 = class1(b5[b7], data[b7])
            self.b4 = class1(b5[b8], data[b8])
        else:
            self.b2 = None
            self.b3 = None
            self.b4 = None
    def fonk2(self, b9 = 0):
        if self.b1 is None:
            return
        print(" " * (b9 * 4) + f"* (Node {self.b1})")
        if self.b3 and self.b3.b1 is not None:
            print(" " * (b9 * 4) + f"  - Inside {self.b1}:")
            self.b3.fonk2(b9 + 1)
        if self.b4 and self.b4.b1 is not None:
            print(" " * (b9 * 4) + f"  - Outside {self.b1}:")
            self.b4.fonk2(b9 + 1)
    def fonk3(self, target_index, a1, data):
        b10 = np.full(a1, -1)
        b6 = np.full(a1, np.inf)
        self.fonk4(target_index, b10, b6, data)
        return b10, b6
    def fonk4(self, target_index, b10, b6, data):
        if self.b1 is None:
            return
        b11 = np.sum((data[self.b1] - data[target_index]) ** 2)
        b12 = b6[-1]
        if target_index != self.b1 and b11 < b12:
            b6[-1] = b11
            b10[-1] = self.b1
            b13 = np.argsort(b6)
            b6[:] = b6[b13]
            b10[:] = b10[b13]
        if self.b2 is None:
            return
        if b11 >= b12 + self.b2:
            self.b4.fonk4(target_index, b10, b6, data)
        elif self.b2 > b12 + b11:
            self.b3.fonk4(target_index, b10, b6, data)
        else:
            self.b3.fonk4(target_index, b10, b6, data)
            self.b4.fonk4(target_index, b10, b6, data)
np.random.seed(42)
b14 = np.random.rand(10, 2)
b15 = np.arange(len(b14))
b16 = class1(b15, b14)
b16.fonk2()
a1 = 3
b10, b6 = b16.fonk3(0, a1, b14)
print("\n3 Nearest Neighbors of the first point:")
print("Indices:", b10)
print("Distances:", b6)