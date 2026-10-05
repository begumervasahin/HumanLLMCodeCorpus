import numpy as np
import math
from scipy.stats import norm
def fonk1(tab):
    return np.min(tab)
def fonk2(tab):
    return np.max(tab)
def fonk3(x):
    return math.pow(x, 3) + (3 * math.pow(x, 2)) + (3 * x) + 1
def fonk4(tab, n):
    return np.mean([fonk3(x) for x in tab])
def fonk5(tab, f_, n):
    return np.sum(np.power(np.array([fonk3(x) for x in tab]) - f_, 2)) / (n - 1)
b1 = np.genfromtxt('RandUnif.csv', delimiter='')
a1 = 2
a2 = 4
b2 = len(b1)
a3 = 0.95
b3 = norm.ppf(a3)
b4 = fonk4(b1, b2)
b5 = fonk5(b1, b4, b2)
b6 = b5 / b2
b7 = (a2 - a1) * (b4 - (b3 * b6))
b8 = (a2 - a1) * (b4 + (b3 * b6))
print(f'Hasil mean-variance (uniform) bag. A\n[{b7}, {b8}]')
b9 = np.genfromtxt('RandDist.csv', delimiter='')
b10 = fonk1(b9)
b11 = fonk2(b9)
b12 = len(b9)
b13 = fonk4(b9, b12)
b14 = fonk5(b9, b13, b12)
b15 = b14 / b12
b16 = (b11 - b10) * (b13 - (b3 * b15))
b17 = (b11 - b10) * (b13 + (b3 * b15))
print(f'Hasil mean-variance (normal) bag. B\n[{b16}, {b17}]')