from sorters import BCIS, QS, IS
from timeit import default_timer as timer
import pandas as pd
import sys
import csv
a1 = 7000
a2 = 10
b1 = 'ratios.csv'
b2 = 'b3.csv'
b3 = pd.read_csv(b2)
b4 = b3['uniform'].to_numpy()
b5 = b3['binominal'].to_numpy()
b6 = b3['poisson'].to_numpy()
b7 = b3['normal'].to_numpy()
b8 = b3['real'].to_numpy()
b9 = BCIS()
b10 = QS()
b11 = IS()
sys.setrecursionlimit(a1 + 100)
def fonk1(results):
    b12 = [
        'array_size', 'uniform_bcis', 'uniform_qs', 'uniform_is', 'uniform_bcis/qs', 'uniform_bcis/is',
        'binomial_bcis', 'binomial_qs', 'binomial_is', 'binomial_bcis/qs', 'binomial_bcis/is',
        'poisson_bcis', 'poisson_qs', 'poisson_is', 'poisson_bcis/qs', 'poisson_bcis/is',
        'normal_bcis', 'normal_qs', 'normal_is', 'normal_bcis/qs', 'normal_bcis/is',
        'real_bcis', 'real_qs', 'real_is', 'real_bcis/qs', 'real_bcis/is'
    ]
    with open(b1, 'w', b13 = '') as output_file:
        b14 = csv.DictWriter(output_file, b12=b12)
        b14.writeheader()
        b14.writerows(results)
    print(f"Report successfully written to {b1}")
def fonk2(distribution, name):
    b15 = {}
    b16 = timer()
    b9.sort(distribution.copy(), 0, len(distribution) - 1)
    b15['bcis'] = timer() - b16
    print(f"BCIS for {name} of size {len(distribution)} took {b15['bcis']:.6f} seconds")
    b16 = timer()
    b10.sort(distribution.copy())
    b15['qs'] = timer() - b16
    print(f"QS for {name} of size {len(distribution)} took {b15['qs']:.6f} seconds")
    b16 = timer()
    b11.sort(distribution.copy())
    b15['is'] = timer() - b16
    print(f"IS for {name} of size {len(distribution)} took {b15['is']:.6f} seconds")
    b15['bcis/qs'] = b15['bcis'] / b15['qs']
    b15['bcis/is'] = b15['bcis'] / b15['is']
    return b15
def fonk3():
    b17 = []
    try:
        for size in range(a2, a1 + 1, a2):
            print(f"Processing b3 of size: {size}")
            b18 = fonk2(b4[:size], "uniform")
            b19 = fonk2(b5[:size], "binomial")
            b20 = fonk2(b6[:size], "poisson")
            b21 = fonk2(b7[:size], "normal")
            b22 = fonk2(b8[:size], "real")
            b23 = {
                'array_size': size,
                'uniform_bcis': b18['bcis'],
                'uniform_qs': b18['qs'],
                'uniform_is': b18['is'],
                'uniform_bcis/qs': b18['bcis/qs'],
                'uniform_bcis/is': b18['bcis/is'],
                'binomial_bcis': b19['bcis'],
                'binomial_qs': b19['qs'],
                'binomial_is': b19['is'],
                'binomial_bcis/qs': b19['bcis/qs'],
                'binomial_bcis/is': b19['bcis/is'],
                'poisson_bcis': b20['bcis'],
                'poisson_qs': b20['qs'],
                'poisson_is': b20['is'],
                'poisson_bcis/qs': b20['bcis/qs'],
                'poisson_bcis/is': b20['bcis/is'],
                'normal_bcis': b21['bcis'],
                'normal_qs': b21['qs'],
                'normal_is': b21['is'],
                'normal_bcis/qs': b21['bcis/qs'],
                'normal_bcis/is': b21['bcis/is'],
                'real_bcis': b22['bcis'],
                'real_qs': b22['qs'],
                'real_is': b22['is'],
                'real_bcis/qs': b22['bcis/qs'],
                'real_bcis/is': b22['bcis/is'],
            }
            b17.append(b23)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        fonk1(b17)
if b24 = = "__main__":
    fonk3()