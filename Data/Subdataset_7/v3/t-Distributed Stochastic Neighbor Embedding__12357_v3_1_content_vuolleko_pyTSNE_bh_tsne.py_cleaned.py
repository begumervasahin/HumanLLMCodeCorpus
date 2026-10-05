import numpy as np
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.a1 = 0.
        self.b3 = np.mean(b2[b1], axis=0)
        if len(b1) > 1:
            self.a1 = np.max(np.linalg.norm(b2[b1] - self.b3, axis=1))
            b4 = b1[b2[b1, 0] < self.b3[0]]
            b5 = b1[b2[b1, 0] >= self.b3[0]]
            self.b6 = class1(b4, b2)
            self.b7 = class1(b5, b2)
        else:
            self.b6 = None
            self.b7 = None
    def fonk2(self, query, neighbors, distances, b2):
        b8 = np.linalg.norm(b2[query] - self.b3)
        if b8 + self.a1 < np.max(distances):
            return
        if self.b6 is None and self.b7 is None:
            b9 = np.linalg.norm(b2[self.b1] - b2[query], axis=1)
            b10 = np.vstack((distances, b9))
            b11 = np.argsort(b10)
            distances[:] = b10[b11[:len(distances)]]
            neighbors[:] = self.b1[b11[:len(neighbors)]]
        else:
            if b2[query, 0] < self.b3[0]:
                self.b6.fonk2(query, neighbors, distances, b2)
                self.b7.fonk2(query, neighbors, distances, b2)
            else:
                self.b7.fonk2(query, neighbors, distances, b2)
                self.b6.fonk2(query, neighbors, distances, b2)
class class2:
    def fonk3(self, b2, b12, b13, b14):
        self.b2 = b2
        self.b12 = b12
        self.b13 = b13
        self.b14 = b14
        self.b15 = []
    def fonk4(self, query, threshold):
        if len(self.b2) == 1:
            b16 = self.b2[0] - query
            b8 = np.linalg.norm(b16)
            if b8 < threshold * self.b14:
                return b16 / b8, 1
            return np.zeros_like(query), 0
        else:
            b17 = np.zeros_like(query)
            a2 = 0.
            for child in self.b15:
                b16, b18 = child.fonk4(query, threshold)
                b17 += b16
                a2 += b18
            return b17, a2
class class3:
    def fonk5(self, *args, **kwargs):
        self.a3 = 0
        self.b2 = None
        self.b19 = None
        self.b20 = None
        self.b21 = None
        self.b22 = None
    def fonk6(self):
        pass
    def fonk7(self, distances):
        pass
    def fonk8(self):
        pass
class class4(class3):
    def fonk9(self, b23 = 0.5, *args, **kwargs):
        self.b23 = b23
        super(class4, self).fonk9(*args, **kwargs)
        self.b22 = 0
    def fonk10(self):
        pass
    def fonk11(self):
        pass
b24 = class4(b23=0.5)
b24.fonk10()
b24.fonk11()