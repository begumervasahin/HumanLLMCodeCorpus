from sorters import BCIS, IS
from timeit import default_timer as timer
import pandas as pd
import csv
a1 = 7000
a2 = 10
b1 = 'ratios.csv'
b2 = 'b3.csv'
b3 = pd.read_csv(b2)
b4 = ['uniform', 'binominal', 'poisson', 'normal', 'real']
b5 = {name: b3[name] for name in b4}
b6 = BCIS()
b7 = IS()
def fonk1(values):
    b8 = b1
    b9 = [
        'array_size',
        'uniform_bcis', 'uniform_qs', 'uniform_is', 'uniform_bcis/qs', 'uniform_bcis/is',
        'binomial_bcis', 'binomial_qs', 'binomial_is', 'binomial_bcis/qs', 'binomial_bcis/is',
        'poisson_bcis', 'poisson_qs', 'poisson_is', 'poisson_bcis/qs', 'poisson_bcis/is',
        'normal_bcis', 'normal_qs', 'normal_is', 'normal_bcis/qs', 'normal_bcis/is',
        'real_bcis', 'real_qs', 'real_is', 'real_bcis/qs', 'real_bcis/is'
    ]
    print('Writing report...')
    with open(b8, 'w', b10 = '') as output_file:
        b11 = csv.DictWriter(output_file, b9=b9)
        b11.writeheader()
        b11.writerows(values)
def fonk2(sorter, distribution, dist_name):
    b12 = timer()
    sorter.sort(distribution)
    b13 = timer()
    b14 = b13 - b12
    print(f"{sorter.__class__.__name__} for size: {len(distribution)} took {b14} for {dist_name}")
    return b14
b15 = []
try:
    for i in range(a2, a1, a2):
        print(f"Array size: {i}")
        b16 = {'array_size': i}
        for dist_name, dist_data in b5.items():
            b17 = fonk2(b6, dist_data[:i], dist_name)
            b18 = fonk2(b7, dist_data[:i], dist_name)
            b16[f'{dist_name}_bcis'] = b17
            b16[f'{dist_name}_qs'] = None
            b16[f'{dist_name}_is'] = b18
            b16[f'{dist_name}_bcis/qs'] = None
            b16[f'{dist_name}_bcis/is'] = b17 / b18
        b15.append(b16)
except Exception as e:
    print("An error occurred:", e)
finally:
    fonk1(b15)