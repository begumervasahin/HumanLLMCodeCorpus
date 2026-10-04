from __future__ import division
import time
import numpy as np
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
        self.b3 = self.fonk2()
        self.fonk3()
        print(self.b2)
    def fonk2(self):
        return lambda S: (5.0 * bp.blsprice(S, self.a8, self.a5, self.a6, self.a4, 'put') +
                          10.0 * bp.rear_end_dnOutCall(S, self.a8, self.a5, self.a6, self.a4, self.a9, self.a7, 0.0))
    def fonk3(self):
        for d in range(self.a1):
            b4 = (self.b3(self.a2 + self.a12) - self.b3(self.a2 - self.a12)) / self.a12
            self.b2[d] = b4
            self.a13 += -self.b3(self.a2) + self.a2 * b4
    def fonk4(self, N_o):
        b5 = self.fonk5()
        b6 = self.fonk6(N_o)
        b7 = self.fonk7(b6, N_o)
        b8 = np.sort(self.a13 - b7)
        print(b8)
        b9 = scs.scoreatpercentile(b8, self.a11 * 100)
        b10 = np.mean(np.maximum(b8 - b9, 0))
        return b9, b10
    def fonk5(self):
        return lambda S: (5.0 * bp.blsprice(S, self.a8, self.a5, self.a6 - self.a7, self.a4, 'put') +
                          10.0 * bp.dnOutCall(S, self.a8, self.a5, self.a6 - self.a7, self.a4, self.a9))
    def fonk6(self, N_o):
        b11 = norm(loc=0, scale=1).ppf(lhs(self.a1, samples=N_o))
        return self.a2 * np.exp((self.a3 - 0.5 * self.a4**2) * self.a7 + self.a4 * np.sqrt(self.a7) * b11)
    def fonk7(self, b6, N_o):
        b7 = np.zeros(N_o)
        for n in range(N_o):
            b7[n] = sum(-self.fonk5()(b6[n, d]) + b6[n, d] * self.b2[d] for d in range(self.a1))
        return b7
if b12 = = "__main__":
    b13 = class1()
    b9, b10 = b13.fonk4(1000)
    print(f"Value at Risk (VaR): {b9}")
    print(f"Expected Excess Loss (EEL): {b10}")