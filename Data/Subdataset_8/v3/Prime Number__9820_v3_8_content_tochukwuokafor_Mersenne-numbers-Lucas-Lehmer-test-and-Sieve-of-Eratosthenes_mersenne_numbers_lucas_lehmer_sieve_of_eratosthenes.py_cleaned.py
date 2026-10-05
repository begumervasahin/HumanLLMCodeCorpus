import math
def mersenne_number(p):
    return (2 ** p) - 1
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
def generate_primes(start, end):
    prime_list = []
    for num in range(start, end):
        if is_prime(num):
            prime_list.append(num)
    return prime_list
def lucas_lehmer_test(p):
    sequence = [4] * (p - 1)
    for i in range(1, p - 1):
        sequence[i] = ((sequence[i - 1] ** 2) - 2) % mersenne_number(p)
    return sequence[p - 2] == 0
def sieve_of_eratosthenes(n):
    is_prime = [False, False] + [True] * (n - 1)
    p = 2
    while p is not None:
        for i in range(2 * p, n + 1, p):
            is_prime[i] = False
        p = next((i for i in range(p + 1, n + 1) if is_prime[i]), None)
    return [i for i, prime in enumerate(is_prime) if prime]
print("Mersenne numbers:")
primes = generate_primes(3, 65)
mersenne_numbers = [mersenne_number(prime) for prime in primes]
print(mersenne_numbers)
print(len(mersenne_numbers))
print("\nLucas-Lehmer test for primality:")
test_primes = generate_primes(3, 65)
test_results = [lucas_lehmer_test(prime) for prime in test_primes]
print(list(zip(test_primes, test_results)))
print("\nSieve of Eratosthenes:")
print(sieve_of_eratosthenes(1000))