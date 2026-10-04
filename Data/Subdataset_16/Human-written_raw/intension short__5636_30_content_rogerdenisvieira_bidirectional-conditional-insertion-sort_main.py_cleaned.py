from sorters import BCIS, QS, IS
from timeit import default_timer as timer
import numpy as np
import pandas as pd
import sys, os, csv, io
a1 = 7000
a2 = 10
b1 = 'ratios.csv'
b2 = 'b3.csv'
b3 = pd.read_csv(b2)
b4 = b3['uniform']
b5 = b3['binominal']
b6 = b3['poisson']
b7 = b3['normal']
b8 = b3['real']
b9 = BCIS()
b10 = IS()
b11 = []
sys.setrecursionlimit(a1+100)
def fonk1(values):
    b12 = b1
    b13 = ['array_size', 'uniform_bcis', 'uniform_qs', 'uniform_is', 'uniform_bcis/qs', 'uniform_bcis/is', 'binomial_bcis', 'binomial_qs', 'binomial_is', 'binomial_bcis/qs', 'binomial_bcis/is', 'poisson_bcis', 'poisson_qs', 'poisson_is', 'poisson_bcis/qs', 'poisson_bcis/is', 'normal_bcis', 'normal_qs', 'normal_is', 'normal_bcis/qs', 'normal_bcis/is','real_bcis', 'real_qs', 'real_is', 'real_bcis/qs', 'real_bcis/is']
    print('Writings report...')
    try:
        b14 = open(b12, 'w', newline='')
        b15 = csv.DictWriter(b14, b13=b13)
        b15.writeheader()
        for row in values:
            b15.writerow(row)
    finally:
        b14.close()
def fonk2(distribution, dist_name):
    b16 = timer()
    b9.sort(distribution, 0, len(distribution)-1)
    b17 = timer()
    b18 = b17 - b16
    print("BCIS for size: {0} took {1} for {2}".format(len(distribution), b18, dist_name))
    b16 = timer()
    b10.sort(distribution)
    b17 = timer()
    b19 = b17 - b16
    print("IS for size: {0} took {1} for {2}".format(len(distribution), b19, dist_name))
    return {
        'bcis' : b18,
        'is' : b19,
        'bcis/is' : (b18/b19)
    }
try:
    for i in range(a2, a1, a2):
        print("Array size: {0}".format(i))
        b20 = fonk2(b4[0:i], "uniform")
        b21 = fonk2(b5[0:i], "binominal")
        b22 = fonk2(b6[0:i], "poisson")
        b23 = fonk2(b7[0:i], "normal")
        b24 = fonk2(b8[0:i], "real")
        b25 = {
            'array_size' : i,
            'uniform_bcis' : b20['bcis'],
            'uniform_is' : b20['is'],
            'uniform_bcis/is' : b20['bcis/is'],
            'binomial_bcis' : b21['bcis'],
            'binomial_is' : b21['is'],
            'binomial_bcis/is' : b21['bcis/is'],
            'poisson_bcis' : b22['bcis'],
            'poisson_is' : b22['is'],
            'poisson_bcis/is' : b22['bcis/is'],
            'normal_bcis' : b23['bcis'],
            'normal_is' : b23['is'],
            'normal_bcis/is' : b23['bcis/is'],
            'real_bcis' : b24['bcis'],
            'real_is' : b24['is'],
            'real_bcis/is' : b24['bcis/is']
        }
        b11.append(b25)
except:
    print("An error has been occurred")
finally:
    fonk1(b11)