from __future__ import division
import numpy as np
from kernels import Kernels
class class1:
    def fonk1(self, b5, b1 = {}):
        self.b2 = b1["n_dims"]
        self.b3 = b1["b3"]
        self.b4 = b1["b4"]
        self.b1 = b1
        self.a1 = 0.4
        self.b5 = b5.copy()
        self.b6 = None
        self.b7 = None
        self.a2 = 0
        (n, b28) = self.b5.shape
        b8 = (n, self.b2)
        min_weight, b9 = (-np.sqrt(6. / sum(b8)), np.sqrt(6. / sum(b8)))
        self.b10 = np.random.randn(n, self.b2) * b9
        self.b11 = None
        self.b12 = np.array([np.zeros_like(self.b10), np.zeros_like(self.b10)])
        np.seterr(b13 = 'ignore', invalid='ignore')
    def fonk2(self):
        b14 = self.b5.copy()
        b15 = self.b1["b15"]
        b16 = self.b1["b16"]
        b17 = self.b1["p_degree"]
        b18 = self.b1["ker"]
        b19 = Kernels(b14, k_opts={"b18": b18, "b16": b16, "b17": b17, "b15": b15})
        self.b5 = b19.process_data()
    def fonk3(self, b5):
        return np.sum(np.abs(b5[:, None] - b5[None, :], b20 = -1))
    def fonk4(self, b5):
        return np.sum((b5[:, None] - b5[None, :]) ** 2, b20 = -1)
    def fonk5(self, b32, target, b21 = 1e-2, max_iterations=1000, b27=1e-10, b26=1e3):
        for i in xrange(max_iterations):
            b22 = (b27 + b26) / 2.
            b23 = np.exp(- (b32) / b22)
            b23 /= np.sum(b23)
            b24 = self.fonk6(b23)
            b25 = np.abs(b24 - target)
            if b25 <= b21:
                break
            if b24 > target:
                b26 = b22
            else:
                b27 = b22
        return b23, b22
    def fonk6(self, b23):
        return -np.sum(b23 * np.log2(b23))
    def fonk7(self):
        n, b28 = self.b5.shape
        b6 = np.zeros((n, n))
        b29 = np.ones((n, 1))
        b30 = self.fonk4(self.b5)
        b31 = np.log2(self.b3)
        for i in xrange(n):
            b32 = b30[i, np.hstack((np.arange(0, i), np.arange(i+1, n)))]
            b23, b22 = self.fonk5(b32, b31)
            b6[i, np.hstack((np.arange(0, i), np.arange(i+1, n)))] = b23
            b29[i] = b22
        b33 = np.mean(np.sqrt(1 / b29))
        print "Mean value of sigma: ", b33
        b6 = (b6 + np.transpose(b6)) / (2 * n)
        b6 /= np.sum(b6)
        b6 = np.maximum(b6, 1e-12)
        return b6
    def fonk8(self):
        b30 = self.fonk4(self.b10)
        b7 = 1 / (1 + b30)
        np.fill_diagonal(b7, 0)
        self.b7 = b7 / np.sum(b7)
        self.b7 = np.maximum(self.b7, 1e-12)
        return b7
    def fonk9(self, b7):
        b34 = self.b6 - self.b7
        b35 = b34 * b7
        b36 = 4 * (np.diag(np.sum(b35, 1)) - b35)
        self.b11 = np.dot(b36, self.b10)
    def fonk10(self, b37 = b39):
        self.fonk2()
        self.b6 = self.fonk7()
        self.b6 *= 10.
        for i in xrange(b37):
            b38 = self.fonk11()
            if i % b39 = = 0:
                print "Iteration ", i, ": b38 is ", b38
        print "b38 : ", b38
        self.b10 = self.b10 - np.mean(self.b10, 0)
        return self.b10
    def fonk11(self):
        b7 = self.fonk8()
        self.fonk9(b7)
        if self.a2 = = 100:
            self.b6 = self.b6 / 10.
        if self.a2 = = 25:
            self.a1 = .8
        self.b10 -= self.b4 * self.b11
        self.b10 += self.a1 * np.diff(self.b12, b20 = 0)[0]
        self.b12[1] = self.b12[0].copy()
        self.b12[0] = self.b10
        b38 = np.sum(self.b6 * np.log(self.b6 / self.b7))
        self.a2 += 1
        return b38