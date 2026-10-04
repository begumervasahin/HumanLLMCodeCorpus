import numpy as np
class class1:
    def fonk1(self, b1, data):
        self.b1 = b1
        self.b2 = data.shape[0]
        self.b3 = data.shape[1]
        self.b4 = None
    def fonk2(self, data, b5 = 10):
        b6 = data.min(b12=0)
        b7 = data.max(b12=0)
        self.b4 = np.random.rand(self.b1, self.b3) * (b7 - b6) + b6
        b8 = np.zeros((self.b1, self.b3))
        a1 = 0
        while not np.allclose(self.b4, b8) and a1 < b5:
            b8 = self.b4.copy()
            a1 += 1
            b9 = np.linalg.norm(data[:, np.newaxis] - self.b4, b12=2)
            b10 = np.argmin(b9, b12=1)
            for i in range(self.b1):
                b11 = data[b10 == i]
                if b11.size > 0:
                    self.b4[i] = b11.mean(b12 = 0)
        return self.b4
    def fonk3(self, data):
        b9 = np.linalg.norm(data[:, np.newaxis] - self.b4, b12=2)
        b10 = np.argmin(b9, b12=1)
        return b10