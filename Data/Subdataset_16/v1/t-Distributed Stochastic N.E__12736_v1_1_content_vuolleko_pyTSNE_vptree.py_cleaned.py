import numpy as np
class class1:
    def fonk1(self, b3, b5):
        if len(b3) == 0:
            self.b1 = None
            self.b2 = None
            return
        self.b1 = b3[0]
        b3 = b3[1:]
        if len(b3) > 0:
            b4 = np.sum((b5[1:, :] - b5[0, :])**2., axis=1)
            b5 = b5[1:, :]
            self.b2 = np.median(b4)
            b6 = b4 < self.b2
            b7 = ~b6
            self.b8 = class1(b3[b6], b5[b6])
            self.b9 = class1(b3[b7], b5[b7])
        else:
            self.b2 = None
            self.b8 = class1([], [])
            self.b9 = class1([], [])
    def fonk2(self, b10 = 0):
        if self.b1 is None:
            return
        b11 = "    " * b10
        print(f"{b11}* (Node {self.b1})")
        if self.b8.b1 is not None:
            print(f"{b11}  - Inside {self.b1}:")
            self.b8.fonk2(b10 + 1)
        if self.b9.b1 is not None:
            print(f"{b11}  - Outside {self.b1}:")
            self.b9.fonk2(b10 + 1)
    def fonk3(self, b1, b18, b4, b5):
        if self.b1 is None:
            return
        b12 = np.sum((b5[self.b1, :] - b5[b1, :])**2.)
        b13 = b4[-1]
        if b1 != self.b1 and b12 < b13:
            b4[-1] = b12
            b18[-1] = self.b1
            b14 = np.argsort(b4)
            b4[:] = b4[b14]
            b18[:] = b18[b14]
        if self.b2 is None:
            return
        if b12 >= b13 + self.b2:
            self.b9.fonk3(b1, b18, b4, b5)
        elif self.b2 > b13 + b12:
            self.b8.fonk3(b1, b18, b4, b5)
        else:
            self.b8.fonk3(b1, b18, b4, b5)
            self.b9.fonk3(b1, b18, b4, b5)
        return b18
np.random.seed(42)
b15 = np.random.rand(10, 2)
b16 = np.arange(len(b15))
b17 = class1(b16, b15)
b17.fonk2()
a1 = 3
b18 = np.full(a1, -1)
b4 = np.full(a1, np.inf)
b17.fonk3(0, b18, b4, b15)
print("\n3 Nearest Neighbors of the first point:")
print("Indices:", b18)
print("Distances:", b4)