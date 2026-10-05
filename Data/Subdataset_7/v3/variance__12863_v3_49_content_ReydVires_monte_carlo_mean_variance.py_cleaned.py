import numpy as np
import math
from scipy.stats import norm
def fonk1(array):
    return np.min(array)
def fonk2(array):
    return np.max(array)
def fonk3(x):
    return math.pow(x, 3) + (3 * math.pow(x, 2)) + (3 * x) + 1
def fonk4(array):
    return np.mean([fonk3(x) for x in array])
def fonk5(array, average_value):
    return np.sum(np.power(np.array([fonk3(x) for x in array]) - average_value, 2)) / (len(array) - 1)
b1 = np.genfromtxt('RandUnif.csv', delimiter='')
b2 = np.genfromtxt('RandDist.csv', delimiter='')
a1 = 2
a2 = 4
b3 = fonk1(b2)
b4 = fonk2(b2)
b5 = len(b1)
b6 = len(b2)
a3 = 0.95
b7 = norm.ppf(a3)
b8 = fonk4(b1)
b9 = fonk5(b1, b8)
b10 = b9 / b5
b11 = (a2 - a1) * (b8 - (b7 * b10))
b12 = (a2 - a1) * (b8 + (b7 * b10))
print(f'Uniform Distribution Results (Bag A): [{b11}, {b12}]')
b13 = fonk4(b2)
b14 = fonk5(b2, b13)
b15 = b14 / b6
b16 = (b4 - b3) * (b13 - (b7 * b15))
b17 = (b4 - b3) * (b13 + (b7 * b15))
print(f'Normal Distribution Results (Bag B): [{b16}, {b17}]')