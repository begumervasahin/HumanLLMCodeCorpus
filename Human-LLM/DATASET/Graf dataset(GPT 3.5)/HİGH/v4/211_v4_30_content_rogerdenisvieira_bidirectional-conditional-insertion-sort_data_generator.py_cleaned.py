import numpy as np
import pandas as pd
import csv
a1 = 7000
a2 = 1
b1 = 'b11.csv'
def fonk1(values):
    b2 = b1
    b3 = ['uniform', 'binomial', 'poisson', 'normal']
    print('Writing data...')
    try:
        with open(b2, 'w', b4 = '') as output_file:
            b5 = csv.DictWriter(output_file, b3=b3)
            b5.writeheader()
            b5.writerows(values)
    except IOError as e:
        print(f"Error writing to file: {e}")
b6 = np.random.uniform(-1, 1, a1)
b7 = np.random.binomial(1000, 0.5, a1)
b8 = np.random.poisson(1000, a1)
b9 = np.random.normal(0, 0.1, a1)
b10 = []
for i in range(0, a1 - 1, a2):
    b11 = {
        'uniform': b6[i],
        'binomial': b7[i],
        'poisson': b8[i],
        'normal': b9[i]
    }
    b10.append(b11)
fonk1(b10)