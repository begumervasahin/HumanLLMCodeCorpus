import numpy as np
import csv
a1 = 7000
a2 = 1
b1 = 'b8.csv'
b2 = ['uniform', 'binominal', 'poisson', 'normal']
def fonk1(test_size):
    b3 = np.random.uniform(-1, 1, test_size)
    b4 = np.random.binomial(1000, 0.5, test_size)
    b5 = np.random.poisson(1000, test_size)
    b6 = np.random.normal(0, 0.1, test_size)
    return b3, b4, b5, b6
def fonk2(b3, b4, b5, b6, step):
    b7 = []
    for i in range(0, len(b3) - 1, step):
        b8 = {
            'uniform': b3[i],
            'binominal': b4[i],
            'poisson': b5[i],
            'normal': b6[i]
        }
        b7.append(b8)
    return b7
def fonk3(b11, filename, fieldnames):
    print('Writing b11...')
    with open(filename, 'w', b9 = '') as output_file:
        b10 = csv.DictWriter(output_file, fieldnames=fieldnames)
        b10.writeheader()
        b10.writerows(b11)
def fonk4():
    b3, b4, b5, b6 = fonk1(a1)
    b11 = fonk2(b3, b4, b5, b6, a2)
    fonk3(b11, b1, b2)
if b12 = = "__main__":
    fonk4()