import time
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def find_mersenne_primes(limit):
    start = time.time()
    primes = [i for i in range(2, limit) if is_prime(i)]
    print(f"Primes up to {limit}: {primes}")
    for prime in primes:
        mersenne_candidate = 2 ** prime - 1
        if is_prime(mersenne_candidate):
            elapsed_time = time.time() - start
            print(f"Time elapsed: {elapsed_time:.2f} seconds")
            mersenne_prime = 2 ** (prime - 1) * mersenne_candidate
            print(f"Mersenne prime: {mersenne_prime}")
if __name__ == "__main__":
    find_mersenne_primes(10000)