import numpy as np
import csv
target = 100
prime = np.array([])
def prime_check(x, prime_list):
    for j in prime_list:
        if j <= np.sqrt(x):
            if x % j == 0:
                return False
        else:
            break
    return True
for i in range(2, target + 1):
    if prime_check(i, prime):
        prime = np.append(prime, i)
with open(f'prime_{target}_({len(prime)}).csv', 'w', newline='') as csvfile:
    prime_writer = csv.writer(csvfile, delimiter=',')
    prime_writer.writerow(prime)
print(f"Target: {target}")
print(f"Number of primes: {len(prime)}")