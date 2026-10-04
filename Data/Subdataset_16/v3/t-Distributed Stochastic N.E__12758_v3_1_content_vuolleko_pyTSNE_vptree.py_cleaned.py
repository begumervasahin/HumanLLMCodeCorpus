import numpy as np
class class1:
    def fonk1(self, b16, data):
        if not b16.size:
            self.b1 = None
            self.b2 = None
            self.b3 = None
            self.b4 = None
            return
        self.b1 = b16[0]
        b5 = b16[1:]
        if b5.size > 0:
            b6 = self.fonk2(data[b5], data[self.b1])
            self.b2 = np.median(b6)
            b7 = b6 < self.b2
            b8 = ~b7
            self.b3 = class1(b5[b7], data[b7])
            self.b4 = class1(b5[b8], data[b8])
        else:
            self.b2 = None
            self.b3 = None
            self.b4 = None
    def fonk2(self, points, center_point):
        return np.sum((points - center_point) ** 2, b9 = 1)
    def fonk3(self, b10 = 0):
        if self.b1 is None:
            return
        print(" " * (b10 * 4) + f"* (Node {self.b1})")
        if self.b3 and self.b3.b1 is not None:
            print(" " * (b10 * 4) + f"  - Inside {self.b1}:")
            self.b3.fonk3(b10 + 1)
        if self.b4 and self.b4.b1 is not None:
            print(" " * (b10 * 4) + f"  - Outside {self.b1}:")
            self.b4.fonk3(b10 + 1)
    def fonk4(self, target_index, a1, data):
        b11 = np.full(a1, -1)
        b6 = np.full(a1, np.inf)
        self.fonk5(target_index, b11, b6, data)
        return b11, b6
    def fonk5(self, target_index, b11, b6, data):
        if self.b1 is None:
            return
        b12 = np.sum((data[self.b1] - data[target_index]) ** 2)
        b13 = b6[-1]
        if target_index != self.b1 and b12 < b13:
            b6[-1] = b12
            b11[-1] = self.b1
            b14 = np.argsort(b6)
            b6[:] = b6[b14]
            b11[:] = b11[b14]
        if self.b2 is None:
            return
        if b12 >= b13 + self.b2:
            self.b4.fonk5(target_index, b11, b6, data)
        elif self.b2 > b13 + b12:
            self.b3.fonk5(target_index, b11, b6, data)
        else:
            self.b3.fonk5(target_index, b11, b6, data)
            self.b4.fonk5(target_index, b11, b6, data)
np.random.seed(42)
b15 = np.random.rand(10, 2)
b16 = np.arange(len(b15))
b17 = class1(b16, b15)
b17.fonk3()
a1 = 3
b11, b6 = b17.fonk4(0, a1, b15)
print("\n3 Nearest Neighbors of the first point:")
print("Indices:", b11)
print("Distances:", b6)