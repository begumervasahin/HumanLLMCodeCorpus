import math
import time
def main():
    n = int(input("Check prime numbers up to: "))
    start = time.time()
    primes = read_primes("output.txt")
    if primes:
        last_prime = primes[-1]
    else:
        last_prime = 2
        primes = [2]
    for x in range(last_prime + 1, n + 1):
        if is_prime(x, primes):
            primes.append(x)
    write_primes("output.txt", primes)
    end = time.time()
    print(f"{end - start} seconds to calculate")
def read_primes(filename):
    try:
        with open(filename, 'r') as file:
            return [int(line.strip()) for line in file]
    except FileNotFoundError:
        return []
def write_primes(filename, primes):
    with open(filename, 'w') as file:
        for prime in primes:
            file.write(f"{prime}\n")
def is_prime(number, primes):
    for prime in primes:
        if prime > math.sqrt(number):
            break
        if number % prime == 0:
            return False
    return True
if __name__ == "__main__":
    main()