import math
import time
def is_prime(number, primes):
    sqrt_number = math.sqrt(number)
    for prime in primes:
        if prime > sqrt_number:
            break
        if number % prime == 0:
            return False
    return True
def main():
    n = int(input("Check prime numbers up to: "))
    start_time = time.time()
    primes = []
    with open('output.txt', 'r') as rf:
        primes = [int(line) for line in rf]
    x = primes[-1] if primes else 2
    while x <= n:
        if is_prime(x, primes):
            primes.append(x)
        x += 1
    with open('output.txt', 'w') as wf:
        for prime in primes:
            wf.write(str(prime) + "\n")
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
if __name__ == "__main__":
    main()