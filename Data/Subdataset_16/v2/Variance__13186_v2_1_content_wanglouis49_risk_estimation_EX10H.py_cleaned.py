from __future__ import division
import time
import numpy as np
import numpy.random as npr
import blspricer as bp
import customML as cm
import scipy.stats as scs
from scipy.stats.distributions import norm
from doe_lhs import lhs
class class1:
    def fonk1(self):
        self.a1 = 10
        self.a2 = 100.0
        self.a3 = 0.08
        self.a4 = 0.3
        self.a5 = 0.05
        self.a6 = 0.1
        self.a7 = 0.04
        self.a8 = 100.0
        self.a9 = 95.0
        self.a10 = 306.8763
        self.a11 = 0.99
        self.b1 = 2**15
        self.a12 = 1e-6
        self.a13 = 0.0
        self.b2 = np.zeros(self.a1)
        self.b3 = lambda S: (5.0 * bp.blsprice(S, self.a8, self.a5, self.a6, self.a4, 'put') +
                                  10.0 * bp.rear_end_dnOutCall(S, self.a8, self.a5, self.a6, self.a4, self.a9, self.a7, 0.0))
        self.fonk2()
        print(self.b2)
    def fonk2(self):
        for d in range(self.a1):
            b4 = (self.b3(self.a2 + self.a12) - self.b3(self.a2 - self.a12)) / self.a12
            self.b2[d] = b4
            self.a13 += -self.b3(self.a2) + self.a2 * b4
    def fonk3(self, N_o):
        b5 = lambda S: (5.0 * bp.blsprice(S, self.a8, self.a5, self.a6 - self.a7, self.a4, 'put') +
                                 10.0 * bp.dnOutCall(S, self.a8, self.a5, self.a6 - self.a7, self.a4, self.a9))
        b6 = norm(loc=0, scale=1).ppf(lhs(self.a1, samples=N_o))
        b7 = self.a2 * np.exp((self.a3 - 0.5 * self.a4**2) * self.a7 + self.a4 * np.sqrt(self.a7) * b6)
        b8 = np.zeros(N_o)
        for n in range(N_o):
            b8[n] = sum(-b5(b7[n, d]) + b7[n, d] * self.b2[d] for d in range(self.a1))
        b9 = np.sort(self.a13 - b8)
        print(b9)
        b10 = scs.scoreatpercentile(b9, self.a11 * 100)
        b11 = np.mean(np.maximum(b9 - b10, 0))
        return b10, b11
if b12 = = "__main__":
    b13 = class1()
    b10, b11 = b13.fonk3(1000)
    print(f"Value at Risk (VaR): {b10}")
    print(f"Expected Excess Loss (EEL): {b11}")