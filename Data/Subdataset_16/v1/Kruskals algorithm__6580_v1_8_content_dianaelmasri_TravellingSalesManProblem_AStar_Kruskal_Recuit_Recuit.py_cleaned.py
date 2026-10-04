import random as rd
import numpy as np
import time
class class1:
    def fonk1(self, file_name):
        self.b1 = self.fonk2(file_name)
    def fonk2(self, file_name):
        with open(file_name, 'r') as file:
            b2 = file.readlines()
            b3 = []
            for line in b2:
                b4 = list(map(int, line.split()))
                b3.append(b4)
            return np.array(b3)
def fonk3(b13, b11):
    a1 = 0
    for b9 in range(len(b13) - 1):
        a1 += b11.b1[b13[b9], b13[b9 + 1]]
    return a1
def fonk4(sol1, b5, b11):
    return fonk3(sol1, b11) - fonk3(b5, b11)
def fonk5(b13, b11, temp):
    b5 = fonk6(b13)
    b6 = fonk4(b5, b13, b11)
    if b6 < 0:
        return b5
    else:
        b7 = rd.random()
        if b7 < np.exp(-b6 / temp):
            return b5
        else:
            return b13
def fonk6(b13):
    b5 = b13.copy()
    b8 = list(range(1, len(b13) - 2))
    b9 = rd.choice(b8)
    b8.remove(b9)
    b10 = rd.choice(b8)
    b5[b9], b5[b10] = b5[b10], b5[b9]
    return b5
def fonk7():
    a2 = 17
    b11 = class1("N17.data")
    a3 = 0
    a4 = 0
    for k in range(10):
        b12 = [b9 for b9 in range(1, a2)]
        rd.shuffle(b12)
        b13 = [0] + b12 + [0]
        a5 = 1000
        b14 = time.time()
        while a5 > 5:
            for b9 in range(a2 ** 2):
                b13 = fonk5(b13, b11, a5)
            a5 *= 0.98
        b15 = time.time() - b14
        print(b13)
        a3 += fonk3(b13, b11)
        a4 += b15
    print(f"Average cost: {a3 / 10}")
    print(f"Average time: {a4 / 10:.2f} seconds")
if b16 = = '__main__':
    fonk7()