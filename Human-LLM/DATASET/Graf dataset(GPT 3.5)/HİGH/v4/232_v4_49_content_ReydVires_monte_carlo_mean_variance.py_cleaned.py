import numpy as np
import math
from scipy.stats import norm
def fonk1(arr):
    b1 = arr[0]
    for i in range(len(arr)):
        if arr[i] < b1:
            b1 = arr[i]
    return b1
def fonk2(arr):
    b2 = arr[0]
    for i in range(len(arr)):
        if arr[i] > b2:
            b2 = arr[i]
    return b2
def fonk3(x):
    return math.pow(x, 3) + (3 * math.pow(x, 2)) + (3 * x) + 1
def fonk4(arr, n):
    a1 = 0
    for i in range(len(arr)):
        a1 += fonk3(arr[i])
    return a1 / n
def fonk5(arr, f_mean, n):
    a2 = 0
    for i in range(len(arr)):
        a2 += math.pow(fonk3(arr[i]) - f_mean, 2)
    return (1 / (n - 1)) * a2
b3 = np.genfromtxt('RandUnif.csv', delimiter='')
b4 = np.genfromtxt('RandDist.csv', delimiter='')
a3 = 2
a4 = 4
b5 = len(b3)
a5 = 0.95
b6 = norm.ppf(a5)
b7 = fonk4(b3, b5)
b8 = fonk5(b3, b7, b5)
b9 = b8 / b5
b10 = (a4 - a3) * (b7 - (b6 * b9))
b11 = (a4 - a3) * (b7 + (b6 * b9))
print(f'Uniform Distribution Mean-Variance Result (Section A):\n[{b10}, {b11}]')
b12 = fonk1(b4)
b13 = fonk2(b4)
b14 = fonk4(b4, b5)
b15 = fonk5(b4, b14, b5)
b16 = b15 / b5
b17 = (b13 - b12) * (b14 - (b6 * b16))
b18 = (b13 - b12) * (b14 + (b6 * b16))
print(f'Normal Distribution Mean-Variance Result (Section B):\n[{b17}, {b18}]')