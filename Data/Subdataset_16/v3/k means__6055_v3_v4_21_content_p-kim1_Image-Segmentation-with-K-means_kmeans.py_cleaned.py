import numpy as np
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.n_data, self.b3 = b2.shape
    def fonk2(self):
        b4 = self.b2.min(b7=0)
        b5 = self.b2.max(b7=0)
        self.b6 = np.random.rand(self.b1, self.b3) * (b5 - b4) + b4
    def fonk3(self, b2, centers):
        return np.linalg.norm(b2[:, np.newaxis] - centers, b7 = 2)
    def fonk4(self, b12):
        for i in range(self.b1):
            b8 = self.b2[b12 == i]
            if b8.size > 0:
                self.b6[i] = b8.mean(b7 = 0)
    def fonk5(self, b9 = 100):
        self.fonk2()
        b10 = np.zeros_like(self.b6)
        a1 = 0
        while np.any(np.abs(b10 - self.b6) > 1e-5) and a1 < b9:
            b10 = self.b6.copy()
            a1 += 1
            b11 = self.fonk3(self.b2, self.b6)
            b12 = np.argmin(b11, b7=1)
            self.fonk4(b12)
        return self.b6
    def fonk6(self, b15):
        b11 = self.fonk3(b15, self.b6)
        b12 = np.argmin(b11, b7=1)
        return b12
if b13 = = "__main__":
    b2 = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
    b1 = 2
    b14 = class1(b1, b2)
    b6 = b14.fonk5(b9=100)
    print("Cluster centers:\n", b6)
    b15 = np.array([[0, 0], [4, 4], [10, 10]])
    b16 = b14.fonk6(b15)
    print("Predicted b16 for new b2:\n", b16)