import numpy as np
import csv
a1 = 7000
a2 = 1
b1 = 'distributions.csv'
b2 = ['uniform', 'binomial', 'poisson', 'b11']
def fonk1(size):
    b3 = np.random.uniform(-1, 1, size)
    b4 = np.random.binomial(1000, 0.5, size)
    b5 = np.random.poisson(1000, size)
    b6 = np.random.b11(0, 0.1, size)
    return b3, b4, b5, b6
def fonk2(uniform, binomial, poisson, b11, step):
    b7 = []
    for i in range(0, len(uniform) - 1, step):
        b8 = {
            'uniform': uniform[i],
            'binomial': binomial[i],
            'poisson': poisson[i],
            'b11': b11[i]
        }
        b7.append(b8)
    return b7
def fonk3(data, filename, fieldnames):
    print('Writing data to CSV...')
    with open(filename, 'w', b9 = '') as csvfile:
        b10 = csv.DictWriter(csvfile, fieldnames=fieldnames)
        b10.writeheader()
        b10.writerows(data)
def fonk4():
    uniform, binomial, poisson, b11 = fonk1(a1)
    b12 = fonk2(uniform, binomial, poisson, b11, a2)
    fonk3(b12, b1, b2)
if b13 = = "__main__":
    fonk4()