import numpy as np
import csv
def fonk1(num, b5):
    for b1 in b5:
        if b1 <= np.sqrt(num):
            if num % b1 = = 0:
                return False
        else:
            break
    return True
def fonk2(a1, b5):
    b2 = f'prime_{a1}_({len(b5)}).csv'
    with open(b2, 'w', b3 = '') as csvfile:
        b4 = csv.writer(csvfile, delimiter=',')
        b4.writerow(b5)
    print(f"Target: {a1}")
    print(f"Number of primes found: {len(b5)}")
def fonk3(a1):
    b5 = []
    for num in range(2, a1 + 1):
        if fonk1(num, b5):
            b5.append(num)
    fonk2(a1, b5)
a1 = 100
fonk3(a1)