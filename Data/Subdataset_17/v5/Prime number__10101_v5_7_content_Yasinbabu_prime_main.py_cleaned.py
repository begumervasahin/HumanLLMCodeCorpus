import numpy as np
import csv
def prime_check(x, prime_list):
    for prime in prime_list:
        if prime > np.sqrt(x):
            break
        if x % prime == 0:
            return False
    return True
def generate_primes_up_to(target):
    primes = np.array([2])
    for i in range(3, target + 1, 2):
        if prime_check(i, primes):
            primes = np.append(primes, i)
    return primes
def save_primes_to_csv(primes, target):
    filename = f'prime_{target}_({len(primes)}).csv'
    with open(filename, 'w', newline='') as csvfile:
        prime_writer = csv.writer(csvfile, delimiter=',')
        prime_writer.writerow(primes)
def main():
    target = 100
    primes = generate_primes_up_to(target)
    save_primes_to_csv(primes, target)
    print(f"Target: {target}")
    print(f"Number of primes found: {len(primes)}")
if __name__ == "__main__":
    main()