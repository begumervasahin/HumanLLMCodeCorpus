import numpy as np
class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
    def fonk2(self, b12):
        if self.b1 is None or self.b1 > b12.shape[0]:
            self.b1 = b12.shape[0]
        self.b2 = np.mean(b12, axis=0)
        b3 = b12 - self.b2
        b4 = np.cov(b3, rowvar=False)
        b7, b5 = np.linalg.eig(b4)
        b6 = np.argsort(b7)[::-1]
        self.b7 = np.real(b7[b6])
        self.b5 = np.real(b5[:, b6])
        b8 = np.sum(self.b7)
        self.b9 = np.cumsum(self.b7) / b8
    def fonk3(self, b12):
        b3 = b12 - self.b2
        b10 = np.dot(b3, self.b5[:, :self.b1])
        return b10
if b11 = = "__main__":
    np.random.seed(0)
    b12 = np.random.rand(10, 5)
    b13 = class1(b1=2)
    b13.fonk2(b12)
    b14 = b13.fonk3(b12)
    print("Original b12 shape:", b12.shape)
    print("Transformed b12 shape:", b14.shape)