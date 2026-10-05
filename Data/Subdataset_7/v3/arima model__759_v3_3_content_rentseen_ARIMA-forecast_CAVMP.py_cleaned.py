from __future__ import print_function
import numpy as np
import random
import math
import time
from statsmodels.tsa.arima.b7 import ARIMA
a1 = 15
a2 = 20
a3 = 150
a4 = 0.06111
a5 = 20
a6 = 0.6
a7 = 16
a8 = 3
a9 = 1
b1 = open("CAVMP_result_4_4_8.txt", "w")
def fonk1(usage_data):
    b2 = a8
    b3 = a9
    b4 = np.log(usage_data)
    b5 = [-1]
    b6 = False
    for i in range(b2, -1, -1):
        if b6:
            break
        for j in range(b3, -1, -1):
            try:
                b7 = ARIMA(b4, order=(i, 0, j))
                b8 = b7.fit(disp=-1)
                b5 = b8.predict(len(usage_data), len(usage_data), dynamic=True)
                b5 = np.exp(b5)
                if math.isnan(b5[0]):
                    continue
                b6 = True
                break
            except:
                continue
    if b5[0] == -1:
        print('Prediction failed!')
    return b5[0] + 0.008
def fonk2():
    b9 = random.randrange(0, 6)
    b10 = [(math.sin(b9 + t) + 1 + a6 * random.random()) * a4 for t in range(a5)]
    return b10
class class1:
    def fonk3(self):
        self.b10 = fonk2()
        self.b11 = len(self.b10)
    def fonk4(self):
        return fonk1(self.b10)
    def fonk5(self, value):
        self.b10.append(value)
        self.b11 += 1
class class2:
    def fonk6(self, b14):
        self.b12 = random.randrange(a1 - 5, a1)
        self.b13 = [class1() for _ in range(self.b12)]
        self.b14 = b14
        self.a10 = -1
    def fonk7(self):
        b15 = sum(vm.fonk4() for vm in self.b13)
        self.a10 = min(b15, 1.0)
class class3:
    def fonk8(self, b16):
        self.b16 = b16
        self.b17 = [class2(b16) for _ in range(a2)]
class class4:
    def fonk9(self):
        self.b10 = 0.07 + 0.06 * random.random()
        self.b18 = []
        self.a11 = -1
b19 = [class3(i) for i in range(a7)]
b20 = set()
for i in range(a7):
    b21 = i
    while True:
        b22 = random.randrange(a7)
        if b22 != b21 and b22 not in b20:
            b20.add(b22)
            b20.add(b21)
            break
b23 = np.zeros((a7, a7))
for b21, b22 in zip(b20, b20):
    b23[b21][b22] = 1
    b23[b22][b21] = 1
b24 = [class4() for _ in range(a3)]
for b32 in b24:
    b25 = random.randrange(min(3, a3 - len(b32.b18)), min(14, a3 - len(b32.b18)) + 1)
    b26 = random.sample(range(a3), b25)
    for dest_index in b26:
        b32.b18.append(dest_index)
for rack in b19:
    for pm in rack.b17:
        pm.fonk7()
b27 = [pm for rack in b19 for pm in rack.b17]
b27.sort(b28 = lambda x: x.a10)
for i, pm in enumerate(b27):
    pm.b29 = i
def fonk10(pm_index1, pm_index2):
    b30 = b27[pm_index1].b14
    b31 = b27[pm_index2].b14
    return b23[b30][b31] == 1
def fonk11(nvm_index, pm_index):
    b32 = b24[nvm_index]
    for dest_index in b32.b18:
        if b27[dest_index].b29 != -1 and not fonk10(dest_index, pm_index):
            return False
    return True
a12 = 0
for b32 in b24:
    for pm_index, pm in enumerate(b27):
        if pm.a10 + b32.b10 < 1:
            if fonk11(nvm_index, pm_index):
                b32.a11 = pm_index
                pm.a10 += b32.b10
                b27.sort(b28 = lambda x: x.a10)
                break
    else:
        a12 += 2
        print("Connect state changed")
        for pm_index, pm in enumerate(b27):
            if pm.a10 + b32.b10 < 1:
                pm.a10 += b32.b10
                break
b27.sort(b28 = lambda x: x.a10)
b33 = b27[0].a10
b34 = b27[-1].a10
b35 = sum(pm.a10 for pm in b27) / len(b27)
b1.write(f"{a12}\t{b33}\t{b35}\t{b34}\n")
print(f"Change count: {a12}")
print(f"Lowest a10: {b33}")
print(f"Average a10: {b35}")
print(f"Highest a10: {b34}")
b1.close()
b36 = time.time()
b37 = b36 - start_time
print("Run time:", b37)