import numpy as np
import csv
def is_prime(x, prime_list):
    for prime_number in prime_list:
        if prime_number <= np.sqrt(x):
            if x % prime_number == 0:
                return False
        else:
            break
    return True
def generate_primes(target):
    primes = []
    for number in range(2, target + 1):
        if is_prime(number, primes):
            primes.append(number)
    return primes
def save_primes_to_csv(primes, target):
    filename = f'prime_{target}_({len(primes)}).csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(primes)
if __name__ == "__main__":
    target = 100
    primes = generate_primes(target)
    save_primes_to_csv(primes, target)
    print("Target:", target)
    print("Number of primes:", len(primes))