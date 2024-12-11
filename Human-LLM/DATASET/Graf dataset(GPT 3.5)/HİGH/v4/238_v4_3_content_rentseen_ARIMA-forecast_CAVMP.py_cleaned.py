from __future__ import print_function
import numpy as np
import pandas as pd
import random
import math
import time
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARIMA
a1 = 15
a2 = 20
a3 = 150
a4 = 0.06111
a5 = 20
a6 = 0.6
a7 = 16
a8 = 3
a9 = 1
def fonk1(origin_data):
    p, b1 = a8, a9
    b2 = np.log(origin_data)
    b3 = [-1]
    for i in range(p, -1, -1):
        for j in range(b1, -1, -1):
            try:
                b4 = ARIMA(b2, order=(i, 0, j))
                b5 = b4.fit(disp=-1)
                b3 = np.exp(b5.fonk4(len(b2), len(b2), dynamic=True))
                if not math.isnan(b3[0]):
                    return b3[0] + 0.008
            except:
                continue
    return b3[0] + 0.008
def fonk2():
    b6 = random.randrange(6)
    return [(math.sin(b6 + t) + 1 + a6 * random.random()) * a4 for t in range(a5)]
class class1:
    def fonk3(self):
        self.b7 = fonk2()
    def fonk4(self):
        return fonk1(self.b7)
class class2:
    def fonk5(self, x):
        self.b8 = random.randrange(a1 - 5, a1)
        self.b9 = [class1() for _ in range(self.b8)]
        self.b10 = x
        self.a10 = -1
    def fonk6(self):
        self.a10 = min(1, sum(vm.fonk4() for vm in self.b9))
class class3:
    def fonk7(self, x):
        self.b11 = [class2(x) for _ in range(a2)]
class class4:
    def fonk8(self):
        self.b7 = 0.07 + 0.06 * random.random()
        self.b12 = []
    def fonk9(self, x):
        self.b12.append(x)
def fonk10():
    b13 = [class3(i) for i in range(a7)]
    b14 = sorted([class4() for _ in range(a3)], key=lambda nvm: nvm.b7, reverse=True)
def fonk11():
    b15 = time.time()
    fonk10()
    b16 = time.time()
    print("Run time:", b16 - b15)
if b17 = = "__main__":
    fonk11()