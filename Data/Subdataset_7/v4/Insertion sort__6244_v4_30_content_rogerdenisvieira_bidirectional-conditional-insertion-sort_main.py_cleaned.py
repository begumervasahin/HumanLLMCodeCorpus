from sorters import BCIS, IS
from timeit import default_timer as timer
import pandas as pd
import csv
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
def fonk1(values):
    b11 = b1
    b12 = [
        'array_size',
        'uniform_bcis', 'uniform_qs', 'uniform_is', 'uniform_bcis/qs', 'uniform_bcis/is',
        'binomial_bcis', 'binomial_qs', 'binomial_is', 'binomial_bcis/qs', 'binomial_bcis/is',
        'poisson_bcis', 'poisson_qs', 'poisson_is', 'poisson_bcis/qs', 'poisson_bcis/is',
        'normal_bcis', 'normal_qs', 'normal_is', 'normal_bcis/qs', 'normal_bcis/is',
        'real_bcis', 'real_qs', 'real_is', 'real_bcis/qs', 'real_bcis/is'
    ]
    print('Writing report...')
    with open(b11, 'w', b13 = '') as output_file:
        b14 = csv.DictWriter(output_file, b12=b12)
        b14.writeheader()
        b14.writerows(values)
def fonk2(distribution, dist_name):
    b15 = timer()
    b9.sort(distribution, 0, len(distribution)-1)
    b16 = timer()
    b17 = b16 - b15
    b18 = timer()
    b10.sort(distribution)
    b19 = timer()
    b20 = b19 - b18
    print(f"BCIS for size: {len(distribution)} took {b17} for {dist_name}")
    print(f"IS for size: {len(distribution)} took {b20} for {dist_name}")
    return {
        'bcis': b17,
        'is': b20,
        'bcis/is': (b17 / b20)
    }
b21 = []
try:
    for i in range(a2, a1, a2):
        print(f"Array size: {i}")
        b22 = fonk2(b4[0:i], "uniform")
        b23 = fonk2(b5[0:i], "binominal")
        b24 = fonk2(b6[0:i], "poisson")
        b25 = fonk2(b7[0:i], "normal")
        b26 = fonk2(b8[0:i], "real")
        b27 = {
            'array_size': i,
            'uniform_bcis': b22['bcis'],
            'uniform_qs': None,
            'uniform_is': b22['is'],
            'uniform_bcis/qs': None,
            'uniform_bcis/is': b22['bcis/is'],
            'binomial_bcis': b23['bcis'],
            'binomial_qs': None,
            'binomial_is': b23['is'],
            'binomial_bcis/qs': None,
            'binomial_bcis/is': b23['bcis/is'],
            'poisson_bcis': b24['bcis'],
            'poisson_qs': None,
            'poisson_is': b24['is'],
            'poisson_bcis/qs': None,
            'poisson_bcis/is': b24['bcis/is'],
            'normal_bcis': b25['bcis'],
            'normal_qs': None,
            'normal_is': b25['is'],
            'normal_bcis/qs': None,
            'normal_bcis/is': b25['bcis/is'],
            'real_bcis': b26['bcis'],
            'real_qs': None,
            'real_is': b26['is'],
            'real_bcis/qs': None,
            'real_bcis/is': b26['bcis/is']
        }
        b21.append(b27)
except Exception as e:
    print("An error occurred:", e)
finally:
    fonk1(b21)