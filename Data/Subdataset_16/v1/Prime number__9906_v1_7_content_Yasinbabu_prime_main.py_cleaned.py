import numpy as np
import csv
a1 = 100
b1 = np.array([])
def fonk1(x, prime_list):
    for b2 in prime_list:
        if b2 <= np.sqrt(x):
            if x % b2 = = 0:
                return False
        else:
            break
    return True
for i in range(2, a1 + 1):
    if fonk1(i, b1):
        b1 = np.append(b1, i)
with open(f'prime_{a1}_({len(b1)}).csv', 'w', b3 = '') as csvfile:
    b4 = csv.writer(csvfile, delimiter=',')
    b4.writerow(b1)
print(f"Target: {a1}")
print(f"Number of primes: {len(b1)}")