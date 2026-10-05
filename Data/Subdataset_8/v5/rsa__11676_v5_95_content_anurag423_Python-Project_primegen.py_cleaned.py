import numpy as np
def prompt_bits():
    bits = int(input('How many bits? '))
    return bits
def generate_prime_list(final):
    primes = list(range(2, final + 1))
    return primes
def sieve_of_eratosthenes(primes):
    for index, prime in enumerate(primes):
        if prime != 0:
            for multiple in range(index + prime, len(primes), prime):
                primes[multiple] = 0
    return primes
def select_random_primes(primes):
    primes = [prime for prime in primes if prime != 0]
    random_primes = np.random.choice(primes, 2)
    return random_primes
def generate_prime_pair():
    bits = prompt_bits()
    final = 2 ** bits
    primes = generate_prime_list(final)
    primes = sieve_of_eratosthenes(primes)
    random_primes = select_random_primes(primes)
    print(f'(Hidden) P Value: {random_primes[0]}')
    print(f'(Hidden) Q Value: {random_primes[1]}')
    return tuple(random_primes)