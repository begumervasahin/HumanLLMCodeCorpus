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
def fonk1(originData):
    b3 = a8
    b4 = a9
    b5 = np.log(originData)
    b6 = [-1]
    b7 = False
    for b28 in range(b3, -1, -1):
        if b7:
            break
        for j in range(b4, -1, -1):
            try:
                b8 = ARIMA(b5, b19=(b28, 0, j))
                b9 = b8.fit(disp=-1)
                b6 = b9.fonk10(len(originData), len(originData), dynamic=True)
                b6 = np.exp(b6)
                if math.isnan(b6[0]):
                    continue
                b7 = True
                break
            except:
                continue
    if b6[0] == -1:
        print('bingo')
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
        self.b13 = fonk2()
        self.b14 = len(self.b13)
    def fonk4(self):
        return fonk1(self.b13)
    def fonk5(self, b10):
        self.b13.append(b10)
        self.b14 = self.b14 + 1
    def fonk6(self):
        print(self.b13)
class class2:
    def fonk7(self, b10):
        self.b14 = random.randrange(a1 - 5, a1)
        self.b15 = []
        self.b16 = b10
        self.a10 = -1
        self.a11 = -1
        for b28 in range(self.b14):
            b17 = class1()
            self.b15.append(b17)
    def fonk8(self, other):
        return self.a10 < other.a10
    def fonk9(self):
        self.a10 = self.fonk10()
    def fonk10(self):
        a12 = 0
        for b28 in range(self.b14):
            a12 = a12 + self.b15[b28].fonk10()
        if a12 > 1:
            a12 = 1
        return a12
    def fonk11(self):
        for b28 in range(self.b14):
            self.b15[b28].fonk13()
class class3:
    def fonk12(self, b10):
        self.b14 = a2
        self.b18 = []
        self.b19 = b10
        for b28 in range(self.b14):
            b3 = class2(self.b19)
            self.b18.append(b3)
    def fonk13(self):
        for b28 in range(self.b14):
            self.b18[b28].fonk13()
            print()
class class4:
    def fonk14(self):
        self.b13 = 0.07 + 0.06 * random.random()
        self.b20 = []
        self.b3 = -1
        self.b14 = 0
    def fonk15(self, other):
        return self.b13 < other.b13
    def fonk16(self, b10):
        self.b20.append(b10)
        self.b14 = self.b14 + 1
    def fonk17(self):
        print(self.b20)
for b28 in range(b30):
    b21 = []
    for b28 in range(a7):
        b12 = class3(b28)
        b21.append(b12)
    b22 = []
    for b28 in range(a7):
        b23 = []
        for j in range(a7):
            b23.append(0)
        b22.append(b23)
    b7 = []
    for b28 in range(a7):
        b7.append(False)
    for b28 in range(a7):
        if b7[b28] == False:
            b7[b28] = True
            while True:
                b12 = random.randrange(0, a7)
                if b7[b12] == False:
                    b7[b12] = True
                    b22[b28][b12] = 1
                    b22[b12][b28] = 1
                    break
    a13 = 8
    b24 = []
    for b28 in range(a3):
        b12 = class4()
        b24.append(b12)
    b24.sort(b25 = True)
    b7 = []
    for b28 in range(a3):
        b7.append(False)
    a14 = 0
    while a14 < a3:
        b26 = random.randrange(min(3, a3 - a14), min(14, a3 - a14) + 1)
        b27 = []
        for b28 in range(b26):
            b10 = random.randrange(0, a3 - a14)
            b10 = b10 + 1
            a15 = 0
            a16 = 0
            while a15 < b10:
                while b7[a16]:
                    a16 = a16 + 1
                a15 = a15 + 1
                a16 = a16 + 1
            b27.append(a16 - 1)
            b7[a16 - 1] = True
            a14 = a14 + 1
        for b28 in range(b26):
            for j in range(b26):
                if b28 = = j:
                    continue
                b24[b27[b28]].fonk16(b27[j])
    b29 = []
    for b28 in range(a7):
        if b28 % b30 = = 0:
            print('b28 = ', b28)
        for j in range(b21[b28].b14):
            b29.append(b21[b28].b18[j])
            b21[b28].b18[j].fonk9()
    b29.sort()
    b31 = len(b29)
    for b28 in range(b31):
        b29[b28].a11 = b28
    def fonk18(b28, j):
        b10 = b29[b28].b16
        b32 = b29[j].b16
        if b10 = = b32:
            return True
        if b22[b10][b32] == 1:
            return True
        return False
    def fonk19(n, b3):
        b7 = False
        a16 = -1
        for b28 in range(b24[n].b14):
            if b24[b24[n].b20[b28]].b3 != -1:
                for k in range(b31):
                    if b29[k].a11 = = b24[b24[n].b20[b28]].b3:
                        a16 = k
                        break
                if not fonk18(a16, b3):
                    b7 = True
                    break
        return b7
    a17 = 0
    b23 = 0
    for b28 in range(a3):
        b23 = 0
        for j in range(b31):
            b23 = b23 + 1
            if b29[j].a10 + b24[b28].b13 < 1:
                if not fonk19(b28, j):
                    b24[b28].b3 = b29[j].a11
                    b29[j].a10 = b29[j].a10 + b24[b28].b13
                    b29.sort()
                    b23 = b23 - 1
                    break
        if b23 = = b31:
            a17 = a17 + 2
            print("connect state changed")
            for j in range(b31):
                if b29[j].a10 + b24[b28].b13 < 1:
                    b29[j].a10 = b29[j].a10 + b24[b28].b13
                    break
    b29.sort()
    b33 = b29[0].a10
    b34 = b29[b31 - 1].a10
    a18 = 0
    for b28 in range(b31):
        a18 = a18 + b29[b28].a10
    b35 = float(a18) / b31
    b2.write(str(a17))
    b2.write('\t')
    b2.write(str(b33))
    b2.write('\t')
    b2.write(str(b35))
    b2.write("\t")
    b2.write(str(b34))
    b2.write("\n")
    print(str(a17))
    print(str(b33))
    print(str(b35))
    print(str(b34))
    print('a17 is ', a17)
b2.close()
b36 = time.time()
print("run time", b36 - b1)