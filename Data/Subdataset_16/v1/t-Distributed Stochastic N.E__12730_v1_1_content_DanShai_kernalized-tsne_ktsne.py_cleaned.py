import numpy as np
from kernels import Kernels
class class1:
    def fonk1(self, b5, b1 = {}):
        self.b2 = b1.get("n_dims", 2)
        self.b3 = b1.get("perplexity", 30)
        self.b4 = b1.get("eta", 200)
        self.b1 = b1
        self.a1 = 0.4
        self.b5 = b5.copy()
        self.b6 = None
        self.b7 = None
        self.a2 = 0
        n, b8 = self.b5.shape
        b9 = (n, self.b2)
        mw, b10 = -np.sqrt(6. / sum(b9)), np.sqrt(6. / sum(b9))
        self.b11 = np.random.randn(n, self.b2) * b10
        self.b12 = None
        self.b13 = np.array([np.zeros_like(self.b11), np.zeros_like(self.b11)])
        np.seterr(b14 = 'ignore', invalid='ignore')
    def fonk2(self):
        b15 = {
            "kernel": self.b1.get("ker", "pca"),
            "gamma": self.b1.get("gamma", 0.5),
            "degree": self.b1.get("p_degree", 1),
            "p_dims": self.b1.get("p_dims", 4)
        }
        b16 = Kernels(self.b5, k_opts=b15)
        self.b5 = b16.process_data()
    @staticmethod
    def fonk3(b5):
        b17 = np.sum(np.abs(b5[:, None] - b5[None, :]), b38=-1)
        return b17
    @staticmethod
    def fonk4(b5):
        b17 = np.sum((b5[:, None] - b5[None, :])**2, b38=-1)
        return b17
    def fonk5(self, b29, target, b18 = 1e-2, niter=1000, b25=1e-10, b24=1e3):
        for i in range(niter):
            b19 = (b25 + b24) / 2.0
            b20 = np.exp(-b29 / b19)
            b21 = np.sum(b20)
            b20 /= b21
            b22 = self.fonk6(b20)
            b23 = np.abs(b22 - target)
            if b23 <= b18:
                break
            if b22 > target:
                b24 = b19
            else:
                b25 = b19
        return b20, b19
    @staticmethod
    def fonk6(b20):
        b26 = -np.sum(b20 * np.log2(b20))
        return b26
    def fonk7(self):
        n, b8 = self.b5.shape
        b6 = np.zeros((n, n))
        b27 = np.ones((n, 1))
        b17 = self.fonk4(self.b5)
        b28 = np.log2(self.b3)
        for i in range(n):
            b29 = b17[i, np.hstack((np.arange(0, i), np.arange(i + 1, n)))]
            b20, b19 = self.fonk5(b29, b28)
            b6[i, np.hstack((np.arange(0, i), np.arange(i + 1, n)))] = b20
            b27[i] = b19
        b30 = np.mean(np.sqrt(1 / b27))
        print("Mean value of sigma:", b30)
        b6 = (b6 + b6.T) / (2 * n)
        b6 = b6 / np.sum(b6)
        b6 = np.maximum(b6, 1e-12)
        return b6
    def fonk8(self):
        b17 = self.fonk4(self.b11)
        b31 = 1 / (1 + b17)
        np.fill_diagonal(b31, 0)
        self.b7 = b31 / np.sum(b31)
        self.b7 = np.maximum(self.b7, 1e-12)
        return b31
    def fonk9(self, b31):
        b32 = self.b6 - self.b7
        b33 = b32 * b31
        b34 = 4 * (np.diag(np.sum(b33, b38=1)) - b33)
        self.b12 = np.dot(b34, self.b11)
    def fonk10(self, b35 = b37):
        self.fonk2()
        self.b6 = self.fonk7()
        self.b6 = self.b6 * 10.0
        for i in range(b35):
            b36 = self.fonk11()
            if i % b37 = = 0:
                print("Iteration", i, ": b36 is", b36)
        print("Final b36:", b36)
        self.b11 = self.b11 - np.mean(self.b11, b38=0)
        return self.b11
    def fonk11(self):
        b31 = self.fonk8()
        self.fonk9(b31)
        if self.a2 = = 100:
            self.b6 = self.b6 / 10.0
        if self.a2 = = 25:
            self.a1 = 0.8
        self.b11 -= self.b4 * self.b12
        self.b11 += self.a1 * np.diff(self.b13, b38 = 0)[0]
        self.b13[1] = self.b13[0].copy()
        self.b13[0] = self.b11
        b39 = np.sum(self.b6 * np.log(self.b6 / self.b7))
        self.a2 += 1
        return b39
if b40 = = "__main__":
    b41 = np.random.rand(100, 10)
    b1 = {
        "n_dims": 2,
        "perplexity": 30,
        "eta": 200,
        "ker": "rbf",
        "gamma": 0.5,
        "p_dims": 50,
        "p_degree": 3
    }
    b42 = class1(b41, b1)
    b43 = b42.fonk10(b35=1000)
    print("Reduced b41 shape:", b43.shape)