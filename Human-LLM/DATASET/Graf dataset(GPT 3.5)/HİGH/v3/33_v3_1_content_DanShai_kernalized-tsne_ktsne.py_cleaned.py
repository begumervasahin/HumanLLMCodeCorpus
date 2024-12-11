from __future__ import division
import numpy as np
from kernels import Kernels
class class1:
    def fonk1(self, b5, b1 = {}):
        self.b2 = b1.get("n_dims", 2)
        self.b3 = b1.get("b3", 30)
        self.b4 = b1.get("b4", 200)
        self.b1 = b1
        self.a1 = 0.4
        self.b5 = b5.copy()
        self.b6 = None
        self.b7 = None
        self.a2 = 0
        self.b8 = None
        self.b9 = None
        self.b10 = np.zeros((2,) + self.b5.shape)
        np.seterr(b11 = 'ignore', invalid='ignore')
    def fonk2(self):
        b12 = {
            "kernel": self.b1.get("ker", "pca"),
            "gamma": self.b1.get("gamma", 0.5),
            "degree": self.b1.get("p_degree", 1),
            "p_dims": self.b1.get("p_dims", 4)
        }
        b13 = Kernels(self.b5.copy(), k_opts=b12)
        self.b5 = b13.process_data()
    def fonk3(self, b5):
        return np.sum(np.abs(b5[:, None] - b5[None, :], b14 = -1))
    def fonk4(self, b5):
        return np.sum((b5[:, None] - b5[None, :]) ** 2, b14 = -1)
    def fonk5(self, b26, target, b15 = 1e-2, max_iterations=1000, b21=1e-10, b20=1e3):
        for _ in range(max_iterations):
            b16 = (b21 + b20) / 2.
            b17 = np.exp(- (b26) / b16)
            b17 /= np.sum(b17)
            b18 = self.fonk6(b17)
            b19 = np.abs(b18 - target)
            if b19 <= b15:
                break
            if b18 > target:
                b20 = b16
            else:
                b21 = b16
        return b17, b16
    def fonk6(self, b17):
        return -np.sum(b17 * np.log2(b17))
    def fonk7(self):
        n, b22 = self.b5.shape
        b6 = np.zeros((n, n))
        b23 = np.ones((n, 1))
        b24 = self.fonk4(self.b5)
        b25 = np.log2(self.b3)
        for i in range(n):
            b26 = b24[i, np.hstack((np.arange(0, i), np.arange(i+1, n)))]
            b17, b16 = self.fonk5(b26, b25)
            b6[i, np.hstack((np.arange(0, i), np.arange(i+1, n)))] = b17
            b23[i] = b16
        b27 = np.mean(np.sqrt(1 / b23))
        print("Mean value of sigma: ", b27)
        b6 = (b6 + b6.T) / (2 * n)
        b6 /= np.sum(b6)
        b6 = np.maximum(b6, 1e-12)
        return b6
    def fonk8(self):
        b24 = self.fonk4(self.b8)
        b7 = 1 / (1 + b24)
        np.fill_diagonal(b7, 0)
        self.b7 = b7 / np.sum(b7)
        self.b7 = np.maximum(self.b7, 1e-12)
        return b7
    def fonk9(self, b7):
        b28 = self.b6 - self.b7
        b29 = b28 * b7
        b30 = 4 * (np.diag(np.sum(b29, 1)) - b29)
        self.b9 = np.dot(b30, self.b8)
    def fonk10(self, b31 = b33):
        self.fonk2()
        self.b6 = self.fonk7()
        self.b6 *= 10.
        for i in range(b31):
            b32 = self.fonk11()
            if i % b33 = = 0:
                print("Iteration ", i, ": b32 is ", b32)
        print("Cost:", b32)
        self.b8 -= np.mean(self.b8, 0)
        return self.b8
    def fonk11(self):
        b7 = self.fonk8()
        self.fonk9(b7)
        if self.a2 = = 100:
            self.b6 /= 10.
        if self.a2 = = 25:
            self.a1 = .8
        self.b8 -= self.b4 * self.b9
        self.b8 += self.a1 * np.diff(self.b10, b14 = 0)[0]
        self.b10[1] = self.b10[0].copy()
        self.b10[0] = self.b8
        b32 = np.sum(self.b6 * np.log(self.b6 / self.b7))
        self.a2 += 1
        return b32