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
b4 = {
    "uniform": b3['uniform'].to_numpy(),
    "binomial": b3['binominal'].to_numpy(),
    "poisson": b3['poisson'].to_numpy(),
    "normal": b3['normal'].to_numpy(),
    "real": b3['real'].to_numpy()
}
b5 = BCIS()
b6 = QS()
b7 = IS()
sys.setrecursionlimit(a1 + 100)
def fonk1(results, b8 = b1):
    b9 = [
        'array_size', 'uniform_bcis', 'uniform_qs', 'uniform_is', 'uniform_bcis/qs', 'uniform_bcis/is',
        'binomial_bcis', 'binomial_qs', 'binomial_is', 'binomial_bcis/qs', 'binomial_bcis/is',
        'poisson_bcis', 'poisson_qs', 'poisson_is', 'poisson_bcis/qs', 'poisson_bcis/is',
        'normal_bcis', 'normal_qs', 'normal_is', 'normal_bcis/qs', 'normal_bcis/is',
        'real_bcis', 'real_qs', 'real_is', 'real_bcis/qs', 'real_bcis/is'
    ]
    with open(b8, 'w', b10 = '') as output_file:
        b11 = csv.DictWriter(output_file, b9=b9)
        b11.writeheader()
        b11.writerows(results)
    print(f"Report successfully written to {b8}")
def fonk2(distribution, name):
    b12 = {}
    for sorter_name, sorter in [("bcis", b5), ("qs", b6), ("is", b7)]:
        b13 = timer()
        sorter.sort(distribution.copy())
        b14 = timer() - b13
        b12[sorter_name] = b14
        print(f"{sorter_name.upper()} for {name} of size {len(distribution)} took {b14:.6f} seconds")
    b12['bcis/qs'] = b12['bcis'] / b12['qs']
    b12['bcis/is'] = b12['bcis'] / b12['is']
    return b12
def fonk3():
    b15 = []
    try:
        for size in range(a2, a1 + 1, a2):
            print(f"Processing b3 of size: {size}")
            b16 = {'array_size': size}
            for name, distribution in b4.items():
                b17 = fonk2(distribution[:size], name)
                b16.update({
                    f"{name}_bcis": b17['bcis'],
                    f"{name}_qs": b17['qs'],
                    f"{name}_is": b17['is'],
                    f"{name}_bcis/qs": b17['bcis/qs'],
                    f"{name}_bcis/is": b17['bcis/is']
                })
            b15.append(b16)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        fonk1(b15)
if b18 = = "__main__":
    fonk3()