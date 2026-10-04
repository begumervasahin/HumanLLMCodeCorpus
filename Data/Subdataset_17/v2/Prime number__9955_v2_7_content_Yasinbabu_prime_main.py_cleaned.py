import numpy as np
import csv
def prime_check(x, prime_list):
    for j in prime_list:
        if j <= np.sqrt(x):
            if x % j == 0:
                return False
        else:
            break
    return True
def find_primes_up_to(target):
    prime_list = np.array([])
    for i in range(2, target + 1):
        if prime_check(i, prime_list):
            prime_list = np.append(prime_list, i)
    return prime_list
def save_primes_to_csv(prime_list, target):
    filename = f'prime_{target}_({len(prime_list)}).csv'
    with open(filename, 'w', newline='') as csvfile:
        prime_writer = csv.writer(csvfile, delimiter=',')
        prime_writer.writerow(prime_list)
    print(f"Primes saved to {filename}")
def main():
    target = 100
    primes = find_primes_up_to(target)
    save_primes_to_csv(primes, target)
    print(f"Target: {target}")
    print(f"Number of primes: {len(primes)}")
if __name__ == "__main__":
    main()