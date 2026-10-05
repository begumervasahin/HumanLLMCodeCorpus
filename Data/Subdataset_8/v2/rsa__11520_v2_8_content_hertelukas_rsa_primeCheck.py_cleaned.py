import math
import time
def main():
    upper_limit = int(input("Please enter a number to check prime numbers up to: "))
    start_time = time.time()
    primes = load_primes_from_file("output.txt")
    last_prime = primes[-1] if primes else 2
    for num in range(last_prime + 1, upper_limit + 1):
        if is_prime(num, primes):
            primes.append(num)
    save_primes_to_file("output.txt", primes)
    end_time = time.time()
    print(f"Prime number generation completed in {end_time - start_time:.2f} seconds.")
def load_primes_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return [int(line.strip()) for line in file]
    except FileNotFoundError:
        return []
def save_primes_to_file(filename, primes):
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