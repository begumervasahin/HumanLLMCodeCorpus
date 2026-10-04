import numpy as np
import csv
def fonk1(x, prime_list):
    for b1 in prime_list:
        if b1 <= np.sqrt(x):
            if x % b1 = = 0:
                return False
        else:
            break
    return True
def fonk2(a1):
    b2 = np.array([2])
    for i in range(3, a1 + 1, 2):
        if fonk1(i, b2):
            b2 = np.append(b2, i)
    return b2
def fonk3(b2, a1):
    b3 = f'prime_{a1}_({len(b2)}).csv'
    with open(b3, 'w', b4 = '') as csvfile:
        b5 = csv.writer(csvfile, delimiter=',')
        b5.writerow(b2)
if b6 = = "__main__":
    a1 = 100
    b2 = fonk2(a1)
    fonk3(b2, a1)
    print(f"Target: {a1}")
    print(f"Number of b2 found: {len(b2)}")