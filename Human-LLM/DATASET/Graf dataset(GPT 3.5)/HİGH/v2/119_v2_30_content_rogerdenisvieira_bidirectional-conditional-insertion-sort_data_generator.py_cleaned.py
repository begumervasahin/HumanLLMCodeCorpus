
import numpy as np
import csv
a1 = 7000
b1 = 'distributions.csv'
def fonk1(values):
    b2 = ['uniform', 'binomial', 'poisson', 'normal']
    print('Writing data...')
    with open(b1, 'w', b3 = '') as output_file:
        b4 = csv.DictWriter(output_file, b2=b2)
        b4.writeheader()
        b4.writerows(values)
    print('Data written successfully.')
def fonk2(size):
    b5 = np.random.uniform(-1, 1, size)
    b6 = np.random.binomial(1000, 0.5, size)
    b7 = np.random.poisson(1000, size)
    b8 = np.random.normal(0, 0.1, size)
    b9 = []
    for i in range(size):
        b9.append({
            'uniform': b5[i],
            'binomial': b6[i],
            'poisson': b7[i],
            'normal': b8[i]
        })
    return b9
def fonk3():
    b9 = fonk2(a1)
    fonk1(b9)
if b10 = = "__main__":
    fonk3()