import numpy as np
import csv
def fonk1(x, b2):
    for b1 in b2:
        if b1 <= np.sqrt(x):
            if x % b1 = = 0:
                return False
        else:
            break
    return True
def fonk2(a1):
    b2 = np.array([])
    for i in range(2, a1 + 1):
        if fonk1(i, b2):
            b2 = np.append(b2, i)
    return b2
def fonk3(b2, a1):
    b3 = f'prime_{a1}_({len(b2)}).csv'
    with open(b3, 'w', b4 = '') as csvfile:
        b5 = csv.writer(csvfile, delimiter=',')
        b5.writerow(b2)
    print(f"Primes saved to {b3}")
def fonk4():
    a1 = 100
    b6 = fonk2(a1)
    fonk3(b6, a1)
    print(f"Target: {a1}")
    print(f"Number of b6: {len(b6)}")
if b7 = = "__main__":
    fonk4()