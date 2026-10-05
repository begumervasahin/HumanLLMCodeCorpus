import numpy as np
import csv
def is_prime(num, prime_list):
    for prime_num in prime_list:
        if prime_num <= np.sqrt(num):
            if num % prime_num == 0:
                return False
        else:
            break
    return True
def save_primes_to_csv(target, prime_list):
    file_name = f'prime_{target}_({len(prime_list)}).csv'
    with open(file_name, 'w', newline='') as csvfile:
        primewriter = csv.writer(csvfile, delimiter=',')
        primewriter.writerow(prime_list)
    print(f"Target: {target}")
    print(f"Number of primes found: {len(prime_list)}")
def find_primes(target):
    prime_list = []
    for num in range(2, target + 1):
        if is_prime(num, prime_list):
            prime_list.append(num)
    save_primes_to_csv(target, prime_list)
target = 100
find_primes(target)