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
b5 = b3['binomial']
b6 = b3['poisson']
b7 = b3['normal']
b8 = b3['real']
b9 = BCIS()
b10 = IS()
def fonk1(values):
    b11 = b1
    b12 = ['array_size', 'uniform_bcis', 'uniform_is', 'binomial_bcis', 'binomial_is', 'poisson_bcis', 'poisson_is', 'normal_bcis', 'normal_is', 'real_bcis', 'real_is']
    print('Writing report...')
    with open(b11, 'w', b13 = '') as output_file:
        b14 = csv.DictWriter(output_file, b12=b12)
        b14.writeheader()
        b14.writerows(values)
def fonk2(sorter, distribution, dist_name):
    b15 = timer()
    sorter.sort(distribution)
    b16 = timer()
    b17 = b16 - b15
    print(f"{sorter.__class__.__name__} for size: {len(distribution)} took {b17} for {dist_name}")
    return b17
try:
    b18 = []
    for i in range(a2, a1 + 1, a2):
        print("Array size:", i)
        b19 = {
            'array_size': i,
            'uniform_bcis': fonk2(b9, b4[:i], "uniform"),
            'uniform_is': fonk2(b10, b4[:i], "uniform"),
            'binomial_bcis': fonk2(b9, b5[:i], "binomial"),
            'binomial_is': fonk2(b10, b5[:i], "binomial"),
            'poisson_bcis': fonk2(b9, b6[:i], "poisson"),
            'poisson_is': fonk2(b10, b6[:i], "poisson"),
            'normal_bcis': fonk2(b9, b7[:i], "normal"),
            'normal_is': fonk2(b10, b7[:i], "normal"),
            'real_bcis': fonk2(b9, b8[:i], "real"),
            'real_is': fonk2(b10, b8[:i], "real")
        }
        b18.append(b19)
except Exception as e:
    print("An error occurred:", e)
finally:
    fonk1(b18)