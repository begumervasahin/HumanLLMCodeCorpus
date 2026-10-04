from __future__ import division
import time
import numpy as np
import numpy.random as npr
import blspricer as bp
import customML as cm
import scipy.stats as scs
from scipy.stats.distributions import norm
from doe_lhs import lhs
class class1(object):
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
        self.b1 = 2 ** 15
        self.a12 = 1e-6
        self.a13 = 0.0
        self.b2 = np.zeros(self.a1)
        self.fonk2()
        print(self.b2)
    def fonk2(self):
        b3 = lambda S: (5.0 * bp.blsprice(S, self.a8, self.a5, self.a6, self.a4, 'put') +
                             10.0 * bp.rear_end_dnOutCall(S, self.a8, self.a5, self.a6, self.a4, self.a9, self.a7, 0.0))
        for d in range(self.a1):
            self.b2[d] = (b3(self.a2 + self.a12) - b3(self.a2 - self.a12)) / self.a12
            self.a13 += -b3(self.a2) + self.a2 * self.b2[d]
    def fonk3(self, N_o):
        ''' Analytical solution '''
        b3 = lambda S: (5.0 * bp.blsprice(S, self.a8, self.a5, self.a6 - self.a7, self.a4, 'put') +
                             10.0 * bp.dnOutCall(S, self.a8, self.a5, self.a6 - self.a7, self.a4, self.a9))
        b4 = norm(loc=0, scale=1).ppf(lhs(self.a1, samples=N_o))
        b5 = np.zeros((N_o, self.a1))
        b5[:, :] = self.a2
        b5[:, :] *= np.exp((self.a3 - 0.5 * self.a4 ** 2) * self.a7 + self.a4 * np.sqrt(self.a7) * b4[:, :])
        b6 = np.zeros(N_o)
        for n in range(N_o):
            for d in range(self.a1):
                b6[n] += -b3(b5[n, d]) + b5[n, d] * self.b2[d]
        b7 = np.sort(self.a13 - b6)
        print(b7)
        b8 = scs.scoreatpercentile(b7, self.a11 * 100.0)
        b9 = np.mean(np.maximum(b7 - b8, 0))
        return b8, b9