import csv
import sys
import pandas as pd
from timeit import default_timer as timer
from sorters import BCIS, IS
a1 = 7000
a2 = 10
b1 = 'ratios.csv'
b2 = 'b3.csv'
sys.setrecursionlimit(a1 + 100)
b3 = pd.read_csv(b2)
b4 = b3['uniform']
b5 = b3['binominal']
b6 = b3['poisson']
b7 = b3['normal']
b8 = b3['real']
b9 = BCIS()
b10 = IS()
def fonk1(distribution, dist_name):
    b11 = timer()
    b9.sort(distribution, 0, len(distribution) - 1)
    b12 = timer() - b11
    print(f"BCIS for size {len(distribution)} took {b12:.5f} seconds for {dist_name}")
    b11 = timer()
    b10.sort(distribution)
    b13 = timer() - b11
    print(f"IS for size {len(distribution)} took {b13:.5f} seconds for {dist_name}")
    return {
        'bcis': b12,
        'is': b13,
        'bcis/is': b12 / b13 if b13 != 0 else float('inf')
    }
def fonk2(data, b14 = b1):
    b15 = [
        'array_size',
        'uniform_bcis', 'uniform_is', 'uniform_bcis/is',
        'binomial_bcis', 'binomial_is', 'binomial_bcis/is',
        'poisson_bcis', 'poisson_is', 'poisson_bcis/is',
        'normal_bcis', 'normal_is', 'normal_bcis/is',
        'real_bcis', 'real_is', 'real_bcis/is'
    ]
    print('Writing report...')
    try:
        with open(b14, 'w', b16 = '') as output_file:
            b17 = csv.DictWriter(output_file, b15=b15)
            b17.writeheader()
            b17.writerows(data)
    except Exception as e:
        print(f"Failed to write report: {e}")
def fonk3():
    b18 = []
    try:
        for i in range(a2, a1, a2):
            print(f"Processing array size: {i}")
            b19 = fonk1(b4[:i], "uniform")
            b20 = fonk1(b5[:i], "binomial")
            b21 = fonk1(b6[:i], "poisson")
            b22 = fonk1(b7[:i], "normal")
            b23 = fonk1(b8[:i], "real")
            b18.append({
                'array_size': i,
                'uniform_bcis': b19['bcis'],
                'uniform_is': b19['is'],
                'uniform_bcis/is': b19['bcis/is'],
                'binomial_bcis': b20['bcis'],
                'binomial_is': b20['is'],
                'binomial_bcis/is': b20['bcis/is'],
                'poisson_bcis': b21['bcis'],
                'poisson_is': b21['is'],
                'poisson_bcis/is': b21['bcis/is'],
                'normal_bcis': b22['bcis'],
                'normal_is': b22['is'],
                'normal_bcis/is': b22['bcis/is'],
                'real_bcis': b23['bcis'],
                'real_is': b23['is'],
                'real_bcis/is': b23['bcis/is']
            })
    except Exception as e:
        print(f"An error occurred during processing: {e}")
    finally:
        fonk2(b18)
if b24 = = "__main__":
    fonk3()