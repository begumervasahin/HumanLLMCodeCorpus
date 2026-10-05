
from __future__ import division
import numpy as np
from kernels import Kernels
class class1:
    def fonk1(self, b5, b1 = {}):
        self.b2 = b1["n_dims"]
        self.b3 = b1["perplexity"]
        self.b4 = b1["eta"]
        self.b1 = b1
        self.a1 = .4
        self.b5 = b5.copy()
        self.b6 = None
        self.b7 = None
        self.a2 = 0
        (n, b30) = self.b5.shape
        b8 = (n, self.b2)
        mw, b9 = (-np.sqrt(6. / sum(b8)), np.sqrt(6. / sum(b8)))
        self.b10 = np.random.randn(n, self.b2)*b9
        self.b11 = None
        self.b12 = np.array(
            [np.zeros_like(self.b10), np.zeros_like(self.b10)])
        np.seterr(b13 = 'ignore', invalid='ignore')
    def fonk2(self):
        b14 = self.b5.copy()
        b15 = self.b1["b15"]
        b16 = self.b1["b16"]
        b17 = self.b1["p_degree"]
        b18 = self.b1["ker"]
        b19 = Kernels(b14, k_opts={
                     "b18": b18, "b16": b16, "b17": b17, "b15": b15})
        self.b5 = b19.process_data()
    def fonk3(self, b5):
        b20 = np.sum(np.abs(b5[:, None] - b5[None, :], -1))
        return b20
    def fonk4(self, b5):
        b20 = np.sum((b5[:, None] - b5[None, :])**2, -1)
        return b20
    def fonk5(self, b33, target, b21 = 1e-2, niter=1000, b28=1e-10, b27=1e3):
        for i in xrange(niter):
            b22 = (b28 + b27)/2.
            b23 = np.exp(- (b33) / b22)
            b24 = np.sum(b23)
            b23 = b23/b24
            b25 = self.fonk6(b23)
            b26 = np.abs(b25-target)
            if b26 <= b21:
                break
            if b25 > target:
                b27 = b22
            else:
                b28 = b22
        return b23, b22
    def fonk6(self, b23):
        b29 = -np.sum(b23*np.log2(b23))
        return b29
    def fonk7(self):
        n, b30 = self.b5.shape
        b6 = np.zeros((n, n))
        b31 = np.ones((n, 1))
        b20 = self.fonk4(self.b5)
        b32 = np.log2(self.b3)
        for i in xrange(n):
            b33 = b20[i, np.hstack((np.arange(0, i), np.arange(i+1, n)))]
            b23, b22 = self.fonk5(b33, b32)
            b6[i, np.hstack((np.arange(0, i), np.arange(i+1, n)))] = b23
            b31[i] = b22
        b34 = np.mean(np.sqrt(1/b31))
        print "Mean value of sigma: ", b34
        b6 = (b6 + np.transpose(b6)) / (2*n)
        b6 = b6 / np.sum(b6)
        b6 = np.maximum(b6, 1e-12)
        return b6
    def fonk8(self):
        b20 = self.fonk4(self.b10)
        b35 = 1 / (1 + b20)
        np.fill_diagonal(b35, 0)
        self.b7 = b35 / np.sum(b35)
        self.b7 = np.maximum(self.b7, 1e-12)
        return b35
    def fonk9(self, b35):
        b36 = self.b6 - self.b7
        b37 = b36 * b35
        b38 = 4 * (np.diag(np.sum(b37, 1)) - b37)
        self.b11 = np.dot(b38, self.b10)
    def fonk10(self, b39 = b41):
        self.fonk2()
        self.b6 = self.fonk7()
        self.b6 = self.b6 * 10.
        for i in xrange(b39):
            b40 = self.fonk11()
            if i % b41 = = 0:
                print "Iteration ", i, ": b40 is ", b40
        print "b40 : ", b40
        self.b10 = self.b10 - np.mean(self.b10, 0)
        return self.b10
    def fonk11(self):
        b35 = self.fonk8()
        self.fonk9(b35)
        if self.a2 = = 100:
            self.b6 = self.b6 / 10.
        if self.a2 = = 25:
            self.a1 = .8
        self.b10 = self.b10 - self.b4*self.b11
        self.b10 = self.b10 + self.a1 * \
            np.diff(self.b12, b42 = 0)[0]
        self.b12[1] = self.b12[0].copy()
        self.b12[0] = self.b10
        b43 = np.sum(self.b6 * np.log(self.b6 / self.b7))
        self.a2 += 1
        return b43