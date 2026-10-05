import numpy as np
class class1:
    def fonk1(self, b1, b12):
        self.b1 = b1
        self.b2 = self.fonk2(b12)
    def fonk2(self, b12):
        minima, b3 = b12.min(b7=0), b12.max(b7=0)
        return np.random.rand(self.b1, b12.shape[1]) * (b3 - minima) + minima
    def fonk3(self, b12):
        b4 = np.sqrt(((b12[:, np.newaxis, :] - self.b2[np.newaxis, :, :]) ** 2).sum(b7=2))
        return b4
    def fonk4(self, b12):
        b4 = self.fonk3(b12)
        b5 = np.argmin(b4, b7=1)
        for i in range(self.b1):
            b6 = b12[b5 == i]
            if len(b6) > 0:
                self.b2[i] = np.mean(b6, b7 = 0)
    def fonk5(self, b12, b8 = 10):
        for _ in range(b8):
            b9 = self.b2.copy()
            self.fonk4(b12)
            if np.allclose(b9, self.b2, b10 = 1e-4):
                break
    def fonk6(self, b12):
        b4 = self.fonk3(b12)
        return np.argmin(b4, b7 = 1)
if b11 = = "__main__":
    b12 = np.random.rand(100, 2)
    b13 = class1(b1=3, b12=b12)
    b13.fonk5(b12)
    b14 = b13.fonk6(b12)
    print("Cluster b2:", b13.b2)
    print("Cluster assignments:", b14)