import numpy as np
import csv
a1 = 7000
a2 = 1
b1 = 'distributions.csv'
def fonk1(data, filename):
    b2 = ['uniform', 'binomial', 'poisson', 'normal']
    print('Writing data to CSV...')
    try:
        with open(filename, 'w', b3 = '') as file:
            b4 = csv.DictWriter(file, b2=b2)
            b4.writeheader()
            b4.writerows(data)
    except IOError as e:
        print(f"Error writing to file: {e}")
b5 = np.random.uniform(-1, 1, a1)
b6 = np.random.binomial(1000, 0.5, a1)
b7 = np.random.poisson(1000, a1)
b8 = np.random.normal(0, 0.1, a1)
b9 = []
for i in range(0, a1 - 1, a2):
    b10 = {
        'uniform': b5[i],
        'binomial': b6[i],
        'poisson': b7[i],
        'normal': b8[i]
    }
    b9.append(b10)
fonk1(b9, b1)