import numpy as np
class class1:
    def fonk1(self, b1, data):
        self.b1 = b1
        self.n_data, self.b2 = data.shape
        self.b3 = None
    def fonk2(self, data, b4 = 10):
        b5 = data.min(b11=0)
        b6 = data.max(b11=0)
        self.b3 = np.random.rand(self.b1, self.b2) * (b6 - b5) + b5
        b7 = np.zeros_like(self.b3)
        a1 = 0
        while not np.allclose(self.b3, b7) and a1 < b4:
            b7 = self.b3.copy()
            a1 += 1
            b8 = np.linalg.norm(data[:, np.newaxis] - self.b3, b11=2)
            b9 = np.argmin(b8, b11=1)
            for i in range(self.b1):
                b10 = data[b9 == i]
                if b10.size > 0:
                    self.b3[i] = b10.mean(b11 = 0)
        return self.b3
    def fonk3(self, data):
        b8 = np.linalg.norm(data[:, np.newaxis] - self.b3, b11=2)
        b9 = np.argmin(b8, b11=1)
        return b9