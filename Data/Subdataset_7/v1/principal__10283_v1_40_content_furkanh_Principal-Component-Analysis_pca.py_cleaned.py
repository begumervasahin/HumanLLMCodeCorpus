import numpy as np
class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
    def fonk2(self, b3):
        if self.b1 is None or self.b1 > b3.shape[0]:
            self.b1 = b3.shape[0]
        b2 = np.mean(b3, axis=0)
        self.b2 = b2
        b3 = b3 - b2
        b4 = np.matmul(b3.transpose(), b3) / (b3.shape[0] - 1)
        b6, b5 = np.linalg.eig(b4)
        b5 = b5[:, b6.argsort()[::-1]]
        b6.sort()
        b6 = b6[::-1]
        self.b6 = np.real(b6)
        self.b5 = np.real(b5)
        self.b7 = []
        b8 = np.sum(self.b6)
        a1 = 0
        for i in range(self.b6.shape[0]):
            a1 += self.b6[i]
            self.b7.append(a1 / b8)
    def fonk3(self, b3):
        b3 = b3 - self.b2
        b9 = np.matmul(b3, self.b5)[:, :self.b1]
        return b9
if b10 = = "__main__":
    np.random.seed(0)
    b3 = np.random.rand(10, 5)
    b11 = class1(b1=2)
    b11.fonk2(b3)
    b12 = b11.fonk3(b3)
    print("Original data shape:", b3.shape)
    print("Transformed data shape:", b12.shape)