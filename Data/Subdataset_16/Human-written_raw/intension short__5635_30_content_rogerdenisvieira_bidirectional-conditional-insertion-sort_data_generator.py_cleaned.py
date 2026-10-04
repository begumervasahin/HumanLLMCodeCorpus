import numpy as np
import pandas as pd
import sys, os, csv, io
a1 = 7000
a2 = 1
b1 = 'b11.csv'
def fonk1(values):
    b2 = b1
    b3 = ['uniform', 'binominal', 'poisson', 'normal']
    print('Writings data...')
    try:
        b4 = open(b2, 'w', newline='')
        b5 = csv.DictWriter(b4, b3=b3)
        b5.writeheader()
        b5.writerows(values)
    finally:
        b4.close()
b6 = np.random.uniform(-1,1,a1)
b7 = np.random.binomial(1000, .5, a1)
b8 = np.random.poisson(1000, a1)
b9 = np.random.normal(0, .1, a1)
b10 = []
for i in range(0, a1-1, a2):
    b11 = {
        'uniform': b6[i],
        'binominal': b7[i],
        'poisson': b8[i],
        'normal': b9[i]
    }
    b10.append(b11)
fonk1(b10)