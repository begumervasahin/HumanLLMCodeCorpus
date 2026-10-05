from numpy import genfromtxt
import math
from scipy.stats import norm
def fonk1(tab):
    b1 = tab[0]
    for i in range(len(tab)):
        if tab[i] < b1:
            b1 = tab[i]
    return b1
def fonk2(tab):
    b2 = tab[0]
    for i in range(len(tab)):
        if tab[i] > b2:
            b2 = tab[i]
    return b2
def fonk3(x):
    return math.pow(x, 3) + (3 * math.pow(x, 2)) + (3 * x) + 1
def fonk4(tab, n):
    a1 = 0
    for i in range(len(tab)):
        a1 += fonk3(tab[i])
    return a1 / n
def fonk5(tab, f_, n):
    a1 = 0
    for i in range(len(tab)):
        a1 += math.pow(fonk3(tab[i]) - f_, 2)
    return (1/(n-1)) * a1
b3 = genfromtxt('RandUnif.csv', delimiter='')
a2 = 2
a3 = 4
b4 = len(b3)
a4 = 0.95
b5 = norm.ppf(a4)
b6 = fonk4(b3, b4)
b7 = fonk5(b3, b6, b4)
b8 = b7/b4
b9 = (a3 - a2) * (b6 - (b5 * b8))
b10 = (a3 - a2) * (b6 + (b5 * b8))
print(f'Hasil mean-variance (uniform) bag. A\n[{b9}, {b10}]')
b3 = genfromtxt('RandDist.csv', delimiter='')
a2 = fonk1(b3)
a3 = fonk2(b3)
b6 = fonk4(b3, b4)
b7 = fonk5(b3, b6, b4)
b8 = b7 / b4
b9 = (a3 - a2) * (b6 - (b5 * b8))
b10 = (a3 - a2) * (b6 + (b5 * b8))
print(f'Hasil mean-variance (normal) bag. B\n[{b9}, {b10}]')