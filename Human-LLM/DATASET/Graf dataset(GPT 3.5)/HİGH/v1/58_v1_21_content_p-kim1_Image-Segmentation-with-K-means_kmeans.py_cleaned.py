import numpy as np
class class1:
    def fonk1(self, b3, b14):
        self.b1 = np.shape(b14)[0]
        self.b2 = np.shape(b14)[1]
        self.b3 = b3
    def fonk2(self, b14, b4 = 10):
        b5 = b14.min(b10=0)
        b6 = b14.max(b10=0)
        self.b7 = np.random.rand(self.b3, self.b2) * (b6 - b5) + b5
        b8 = np.random.rand(self.b3, self.b2) * (b6 - b5) + b5
        a1 = 0
        while np.sum(np.sum(b8 - self.b7)) != 0 and a1 < b4:
            b8 = self.b7.copy()
            a1 += 1
            b9 = np.ones((self.b3, self.b1)) * np.sum((b14 - self.b7[0, :]) ** 2, b10=1)
            for j in range(1, self.b3):
                b9[j, :] = np.sum((b14 - self.b7[j, :]) ** 2, b10 = 1)
            b11 = np.argmin(b9, b10=0)
            for j in range(self.b3):
                b12 = (b11 == j)
                if np.sum(b12) > 0:
                    self.b7[j, :] = np.sum(b14[b12, :], b10 = 0) / np.sum(b12)
        return self.b7
    def fonk3(self, b14):
        b1 = np.shape(b14)[0]
        b9 = np.ones((self.b3, b1)) * np.sum((b14 - self.b7[0, :]) ** 2, b10=1)
        for j in range(1, self.b3):
            b9[j, :] = np.sum((b14 - self.b7[j, :]) ** 2, b10 = 1)
        b11 = np.argmin(b9, b10=0)
        return b11
if b13 = = "__main__":
    np.random.seed(42)
    b14 = np.random.rand(100, 2)
    b15 = class1(b3=3, b14=b14)
    b16 = b15.fonk2(b14)
    print("Final b16:")
    print(b16)
    b17 = np.random.rand(10, 2)
    b18 = b15.fonk3(b17)
    print("Clusters for new b14:")
    print(b18)