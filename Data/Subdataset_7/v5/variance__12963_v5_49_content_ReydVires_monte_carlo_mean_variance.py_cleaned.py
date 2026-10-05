import numpy as np
import math
from scipy.stats import norm
def fonk1(arr):
    return min(arr)
def fonk2(arr):
    return max(arr)
def fonk3(x):
    return x**3 + 3*x**2 + 3*x + 1
def fonk4(arr):
    return np.mean([fonk3(x) for x in arr])
def fonk5(arr, f_mean):
    return np.var([fonk3(x) for x in arr], b1 = 1)
b2 = np.genfromtxt('RandUnif.csv', delimiter='')
b3 = np.genfromtxt('RandDist.csv', delimiter='')
a1 = 2
a2 = 4
b4 = len(b2)
a3 = 0.95
b5 = norm.ppf(a3)
b6 = fonk4(b2)
b7 = fonk5(b2, b6)
b8 = b7 / b4
b9 = (a2 - a1) * (b6 - (b5 * b8))
b10 = (a2 - a1) * (b6 + (b5 * b8))
print(f'Uniform Distribution Mean-Variance Result (Section A):\n[{b9}, {b10}]')
b11 = fonk1(b3)
b12 = fonk2(b3)
b13 = fonk4(b3)
b14 = fonk5(b3, b13)
b15 = b14 / b4
b16 = (b12 - b11) * (b13 - (b5 * b15))
b17 = (b12 - b11) * (b13 + (b5 * b15))
print(f'Normal Distribution Mean-Variance Result (Section B):\n[{b16}, {b17}]')