import numpy as np
from kernels import Kernels
class class1:
    def fonk1(self, b5, b1 = None):
        if b1 is None:
            b1 = {}
        self.b2 = b1.get("n_dims", 2)
        self.b3 = b1.get("perplexity", 30)
        self.b4 = b1.get("eta", 200)
        self.b1 = b1
        self.a1 = 0.4
        self.a2 = 0
        self.b5 = b5.copy()
        self.b6 = None
        self.b7 = None
        self.b8 = None
        n, b9 = self.b5.shape
        self.b10 = np.random.randn(n, self.b2) * np.sqrt(6. / sum((n, self.b2)))
        self.b11 = np.array([np.zeros_like(self.b10), np.zeros_like(self.b10)])
        np.seterr(b12 = 'ignore', invalid='ignore')
    def fonk2(self):
        b13 = {
            "kernel": self.b1.get("ker", "pca"),
            "gamma": self.b1.get("gamma", 0.5),
            "degree": self.b1.get("p_degree", 1),
            "p_dims": self.b1.get("p_dims", 4)
        }
        b14 = Kernels(self.b5, k_opts=b13)
        self.b5 = b14.process_data()
    @staticmethod
    def fonk3(b5):
        return np.sum(np.abs(b5[:, None] - b5[None, :]), b15 = -1)
    @staticmethod
    def fonk4(b5):
        return np.sum((b5[:, None] - b5[None, :])**2, b15 = -1)
    def fonk5(self, b26, target, b16 = 1e-2, niter=1000, b22=1e-10, b21=1e3):
        for _ in range(niter):
            b17 = (b22 + b21) / 2.0
            b18 = np.exp(-b26 / b17)
            b18 /= np.sum(b18)
            b19 = self.fonk6(b18)
            b20 = np.abs(b19 - target)
            if b20 <= b16:
                break
            if b19 > target:
                b21 = b17
            else:
                b22 = b17
        return b18, b17
    @staticmethod
    def fonk6(b18):
        return -np.sum(b18 * np.log2(b18))
    def fonk7(self):
        n, b9 = self.b5.shape
        b6 = np.zeros((n, n))
        b23 = np.ones((n, 1))
        b24 = self.fonk4(self.b5)
        b25 = np.log2(self.b3)
        for i in range(n):
            b26 = b24[i, np.hstack((np.arange(0, i), np.arange(i + 1, n)))]
            b18, b27 = self.fonk5(b26, b25)
            b6[i, np.hstack((np.arange(0, i), np.arange(i + 1, n)))] = b18
            b23[i] = b27
        b6 = (b6 + b6.T) / (2 * n)
        b6 = b6 / np.sum(b6)
        b6 = np.maximum(b6, 1e-12)
        b28 = np.mean(np.sqrt(1 / b23))
        print("Mean value of b27:", b28)
        return b6
    def fonk8(self):
        b24 = self.fonk4(self.b10)
        b29 = 1 / (1 + b24)
        np.fill_diagonal(b29, 0)
        self.b7 = b29 / np.sum(b29)
        self.b7 = np.maximum(self.b7, 1e-12)
        return b29
    def fonk9(self, b29):
        b30 = self.b6 - self.b7
        b31 = b30 * b29
        b32 = 4 * (np.diag(np.sum(b31, b15=1)) - b31)
        self.b8 = np.dot(b32, self.b10)
    def fonk10(self, b33 = b35):
        self.fonk2()
        self.b6 = self.fonk7() * 10.0
        for i in range(b33):
            b34 = self.fonk11()
            if i % b35 = = 0:
                print(f"Iteration {i}: b34 is {b34}")
        print("Final b34:", b34)
        self.b10 -= np.mean(self.b10, b15 = 0)
        return self.b10
    def fonk11(self):
        b29 = self.fonk8()
        self.fonk9(b29)
        if self.a2 = = 100:
            self.b6 /= 10.0
        if self.a2 = = 25:
            self.a1 = 0.8
        self.b10 -= self.b4 * self.b8
        self.b10 += self.a1 * np.diff(self.b11, b15 = 0)[0]
        self.b11[1] = self.b11[0].copy()
        self.b11[0] = self.b10
        b36 = np.sum(self.b6 * np.log(self.b6 / self.b7))
        self.a2 += 1
        return b36
if b37 = = "__main__":
    b38 = np.random.rand(100, 10)
    b1 = {
        "n_dims": 2,
        "perplexity": 30,
        "eta": 200,
        "ker": "rbf",
        "gamma": 0.5,
        "p_dims": 50,
        "p_degree": 3
    }
    b39 = class1(b38, b1)
    b40 = b39.fonk10(b33=1000)
    print("Reduced b38 shape:", b40.shape)