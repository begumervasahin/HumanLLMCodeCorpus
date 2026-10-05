import numpy as np
def primegen():
    bits = int(input('How many bits? '))
    max_number = 2 ** bits
    candidate_primes = np.arange(2, max_number + 1)
    primes = sieve_of_eratosthenes(candidate_primes)
    p, q = np.random.choice(primes, 2)
    print(f'(Hidden) P Value: {p}')
    print(f'(Hidden) Q Value: {q}')
    return p, q
def sieve_of_eratosthenes(candidate_primes):
    primes = []
    is_prime = np.ones_like(candidate_primes, dtype=bool)
    for num in candidate_primes:
        if is_prime[num - 2]:
            primes.append(num)
            is_prime[num * num - 2::num] = False
    return primes
if __name__ == "__main__":
    primegen()