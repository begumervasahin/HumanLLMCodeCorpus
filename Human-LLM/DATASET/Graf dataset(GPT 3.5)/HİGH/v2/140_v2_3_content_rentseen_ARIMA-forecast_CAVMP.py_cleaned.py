from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
from matplotlib.pylab import rcParams
from statsmodels.tsa.arima.b8 import ARIMA
import random
import math
import time
b1 = time.time()
a1 = 15
a2 = 20
a3 = 150
a4 = 0.06111
a5 = 20
a6 = 0.6
a7 = 16
a8 = 3
a9 = 1
b2 = open("CAVMP_result_4_4_8.txt", "w")
def fonk1(origin_data):
    b3 = a8
    b4 = a9
    b5 = np.log(origin_data)
    b6 = [-1]
    b7 = False
    for i in range(b3, -1, -1):
        if b7:
            break
        for j in range(b4, -1, -1):
            try:
                b8 = ARIMA(b5, order=(i, 0, j))
                b9 = b8.fit(disp=-1)
                b6 = b9.predict(len(origin_data), len(origin_data), dynamic=True)
                b6 = np.exp(b6)
                if math.isnan(b6[0]):
                    continue
                b7 = True
                break
            except:
                continue
    if b6[0] == -1:
        print('Prediction failed!')
    return b6[0] + 0.008
def fonk2():
    b10 = []
    b11 = random.randrange(0, 6)
    for t in range(a5):
        b12 = (math.sin(b11 + t) + 1 + a6 * random.random()) * a4
        b10.append(b12)
    return b10
class class1:
    def fonk3(self):
        self.b10 = fonk2()
        self.b13 = len(self.b10)
    def fonk4(self):
        return fonk1(self.b10)
    def fonk5(self, b12):
        self.b10.append(b12)
        self.b13 += 1
class class2:
    def fonk6(self, b16):
        self.b14 = random.randrange(a1 - 5, a1)
        self.b15 = [class1() for _ in range(self.b14)]
        self.b16 = b16
        self.a10 = -1
    def fonk7(self):
        b17 = sum(vm.fonk4() for vm in self.b15)
        self.a10 = min(b17, 1.0)
class class3:
    def fonk8(self, b18):
        self.b18 = b18
        self.b19 = [class2(b18) for _ in range(a2)]
class class4:
    def fonk9(self):
        self.b10 = 0.07 + 0.06 * random.random()
        self.b20 = []
        self.a11 = -1
b21 = [class3(i) for i in range(a7)]
b22 = set()
for i in range(a7):
    b23 = i
    while True:
        b24 = random.randrange(a7)
        if b24 != b23 and b24 not in b22:
            b22.add(b24)
            b22.add(b23)
            break
b25 = np.zeros((a7, a7))
for b23, b24 in zip(b22, b22):
    b25[b23][b24] = 1
    b25[b24][b23] = 1
b26 = [class4() for _ in range(a3)]
for b34 in b26:
    b27 = random.randrange(min(3, a3 - len(b34.b20)), min(14, a3 - len(b34.b20)) + 1)
    b28 = random.sample(range(a3), b27)
    for dest_index in b28:
        b34.b20.append(dest_index)
for rack in b21:
    for pm in rack.b19:
        pm.fonk7()
b29 = [pm for rack in b21 for pm in rack.b19]
b29.sort(b30 = lambda x: x.a10)
for i, pm in enumerate(b29):
    pm.b31 = i
def fonk10(pm_index1, pm_index2):
    b32 = b29[pm_index1].b16
    b33 = b29[pm_index2].b16
    return b25[b32][b33] == 1
def fonk11(nvm_index, pm_index):
    b34 = b26[nvm_index]
    for dest_index in b34.b20:
        if b29[dest_index].b31 != -1 and not fonk10(dest_index, pm_index):
            return False
    return True
a12 = 0
for b34 in b26:
    for pm_index, pm in enumerate(b29):
        if pm.a10 + b34.b10 < 1:
            if fonk11(nvm_index, pm_index):
                b34.a11 = pm_index
                pm.a10 += b34.b10
                b29.sort(b30 = lambda x: x.a10)
                break
    else:
        a12 += 2
        print("Connect state changed")
        for pm_index, pm in enumerate(b29):
            if pm.a10 + b34.b10 < 1:
                pm.a10 += b34.b10
                break
b29.sort(b30 = lambda x: x.a10)
b35 = b29[0].a10
b36 = b29[-1].a10
b37 = sum(pm.a10 for pm in b29) / len(b29)
b2.write(f"{a12}\t{b35}\t{b37}\t{b36}\n")
print(f"Change count: {a12}")
print(f"Lowest a10: {b35}")
print(f"Average a10: {b37}")
print(f"Highest a10: {b36}")
b2.close()
b38 = time.time()
b39 = b38 - b1
print("Run time:", b39)