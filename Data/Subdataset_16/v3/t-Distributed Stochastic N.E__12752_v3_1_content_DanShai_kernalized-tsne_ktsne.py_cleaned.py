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
        b23, b9 = self.b5.shape
        self.b10 = np.random.randn(b23, self.b2) * np.sqrt(6. / sum((b23, self.b2)))
        self.b11 = np.zeros((2, b23, self.b2))
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
    def fonk5(self, b27, target, b16 = 1e-2, niter=1000, b22=1e-10, b21=1e3):
        for _ in range(niter):
            b17 = (b22 + b21) / 2.0
            b18 = np.exp(-b27 / b17)
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
        b23 = self.b5.shape[0]
        b6 = np.zeros((b23, b23))
        b24 = np.ones((b23, 1))
        b25 = self.fonk4(self.b5)
        b26 = np.log2(self.b3)
        for i in range(b23):
            b27 = b25[i, np.hstack((np.arange(0, i), np.arange(i + 1, b23)))]
            b18, b28 = self.fonk5(b27, b26)
            b6[i, np.hstack((np.arange(0, i), np.arange(i + 1, b23)))] = b18
            b24[i] = b28
        b6 = (b6 + b6.T) / (2 * b23)
        b6 /= np.sum(b6)
        b6 = np.maximum(b6, 1e-12)
        b29 = np.mean(np.sqrt(1 / b24))
        print("Mean value of b28:", b29)
        return b6
    def fonk8(self):
        b25 = self.fonk4(self.b10)
        b30 = 1 / (1 + b25)
        np.fill_diagonal(b30, 0)
        self.b7 = b30 / np.sum(b30)
        self.b7 = np.maximum(self.b7, 1e-12)
        return b30
    def fonk9(self, b30):
        b31 = self.b6 - self.b7
        b32 = b31 * b30
        b33 = 4 * (np.diag(np.sum(b32, b15=1)) - b32)
        self.b8 = np.dot(b33, self.b10)
    def fonk10(self, b34 = b36):
        self.fonk2()
        self.b6 = self.fonk7() * 10.0
        for i in range(b34):
            b35 = self.fonk11()
            if i % b36 = = 0:
                print(f"Iteration {i}: b35 is {b35}")
        print("Final b35:", b35)
        self.b10 -= np.mean(self.b10, b15 = 0)
        return self.b10
    def fonk11(self):
        b30 = self.fonk8()
        self.fonk9(b30)
        if self.a2 = = 100:
            self.b6 /= 10.0
        if self.a2 = = 25:
            self.a1 = 0.8
        self.b10 -= self.b4 * self.b8
        self.b10 += self.a1 * np.diff(self.b11, b15 = 0)[0]
        self.b11[1] = self.b11[0].copy()
        self.b11[0] = self.b10
        b37 = np.sum(self.b6 * np.log(self.b6 / self.b7))
        self.a2 += 1
        return b37
if b38 = = "__main__":
    b39 = np.random.rand(100, 10)
    b1 = {
        "n_dims": 2,
        "perplexity": 30,
        "eta": 200,
        "ker": "rbf",
        "gamma": 0.5,
        "p_dims": 50,
        "p_degree": 3
    }
    b40 = class1(b39, b1)
    b41 = b40.fonk10(b34=1000)
    print("Reduced b39 shape:", b41.shape)