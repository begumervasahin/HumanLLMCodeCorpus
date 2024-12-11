import numpy as np
import csv
a1 = 7000
b1 = 'b4.csv'
def fonk1(values, filename, fieldnames):
    print('Writing data to CSV...')
    with open(filename, 'w', b2 = '') as file:
        b3 = csv.DictWriter(file, fieldnames=fieldnames)
        b3.writeheader()
        b3.writerows(values)
    print('Data successfully written to', filename)
def fonk2(sample_size):
    return {
        'uniform': np.random.uniform(-1, 1, sample_size),
        'binomial': np.random.binomial(1000, 0.5, sample_size),
        'poisson': np.random.poisson(1000, sample_size),
        'normal': np.random.normal(0, 0.1, sample_size)
    }
def fonk3(sample_size):
    b4 = fonk2(sample_size)
    b5 = [
        {dist: b4[dist][i] for dist in b4}
        for i in range(sample_size)
    ]
    return b5
def fonk4():
    b6 = fonk3(a1)
    b7 = ['uniform', 'binomial', 'poisson', 'normal']
    fonk1(b6, b1, b7)
if b8 = = "__main__":
    fonk4()