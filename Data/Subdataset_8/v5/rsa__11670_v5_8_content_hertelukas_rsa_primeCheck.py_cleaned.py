import math
import time
def main():
    upper_limit = get_upper_limit()
    start_time = time.time()
    primes = load_primes_from_file("output.txt")
    last_prime = get_last_prime(primes)
    generate_new_primes(last_prime, upper_limit, primes)
    save_primes_to_file("output.txt", primes)
    end_time = time.time()
    print_generation_time(start_time, end_time)
def get_upper_limit():
    return int(input("Please enter the upper limit for prime number generation: "))
def load_primes_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return [int(line.strip()) for line in file]
    except FileNotFoundError:
        return []
def get_last_prime(primes):
    return primes[-1] if primes else 2
def generate_new_primes(last_prime, upper_limit, primes):
    for num in range(last_prime + 1, upper_limit + 1):
        if is_prime(num, primes):
            primes.append(num)
def is_prime(number, primes):
    for prime in primes:
        if prime > math.sqrt(number):
            break
        if number % prime == 0:
            return False
    return True
def save_primes_to_file(filename, primes):
    with open(filename, 'w') as file:
        for prime in primes:
            file.write(f"{prime}\n")
def print_generation_time(start_time, end_time):
    generation_time = end_time - start_time
    print(f"Prime number generation completed in {generation_time:.2f} seconds.")
if __name__ == "__main__":
    main()