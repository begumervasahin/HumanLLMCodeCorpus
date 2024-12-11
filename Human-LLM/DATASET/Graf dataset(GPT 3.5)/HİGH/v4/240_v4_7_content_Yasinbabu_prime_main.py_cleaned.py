import numpy as np
import csv
def fonk1(num, b2):
    for b1 in b2:
        if b1 <= np.sqrt(num):
            if num % b1 = = 0:
                return False
        else:
            break
    return True
a1 = 100
b2 = np.array([])
for num in range(2, a1 + 1):
    if fonk1(num, b2):
        b2 = np.append(b2, num)
b3 = f'prime_{a1}_({len(b2)}).csv'
with open(b3, 'w', b4 = '') as csvfile:
    b5 = csv.writer(csvfile, delimiter=',')
    b5.writerow(b2)
print(f"Target: {a1}")
print(f"Number of primes found: {len(b2)}")