import numpy as np
import csv
a1 = 7000
a2 = 1
b1 = 'distributions.csv'
b2 = ['b3', 'b4', 'b5', 'b6']
def fonk1(size):
    b3 = np.random.b3(-1, 1, size)
    b4 = np.random.binomial(1000, 0.5, size)
    b5 = np.random.b5(1000, size)
    b6 = np.random.b6(0, 0.1, size)
    return b3, b4, b5, b6
def fonk2(b3, b4, b5, b6, step):
    b7 = []
    for i in range(0, len(b3) - 1, step):
        b7.append({
            'b3': b3[i],
            'b4': b4[i],
            'b5': b5[i],
            'b6': b6[i]
        })
    return b7
def fonk3(b7, filename, fieldnames):
    print('Writing b7 to CSV...')
    with open(filename, 'w', b8 = '') as csvfile:
        b9 = csv.DictWriter(csvfile, fieldnames=fieldnames)
        b9.writeheader()
        b9.writerows(b7)
def fonk4():
    b3, b4, b5, b6 = fonk1(a1)
    b7 = fonk2(b3, b4, b5, b6, a2)
    fonk3(b7, b1, b2)
if b10 = = "__main__":
    fonk4()