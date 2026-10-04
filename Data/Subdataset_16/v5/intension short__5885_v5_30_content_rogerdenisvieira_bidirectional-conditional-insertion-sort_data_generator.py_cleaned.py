import numpy as np
import csv
a1 = 7000
a2 = 1
b1 = 'b11.csv'
def fonk1(values, filename):
    b2 = ['uniform', 'binomial', 'poisson', 'normal']
    print('Writing data to file...')
    with open(filename, 'w', b3 = '') as output_file:
        b4 = csv.DictWriter(output_file, b2=b2)
        b4.writeheader()
        b4.writerows(values)
    print(f'Data successfully written to {filename}.')
def fonk2(test_size, step):
    b5 = np.random.uniform(-1, 1, test_size)
    b6 = np.random.binomial(1000, 0.5, test_size)
    b7 = np.random.poisson(1000, test_size)
    b8 = np.random.normal(0, 0.1, test_size)
    b9 = [
        {
            'uniform': b5[i],
            'binomial': b6[i],
            'poisson': b7[i],
            'normal': b8[i]
        }
        for i in range(0, test_size, step)
    ]
    return b9
if b10 = = "__main__":
    b11 = fonk2(a1, a2)
    fonk1(b11, b1)