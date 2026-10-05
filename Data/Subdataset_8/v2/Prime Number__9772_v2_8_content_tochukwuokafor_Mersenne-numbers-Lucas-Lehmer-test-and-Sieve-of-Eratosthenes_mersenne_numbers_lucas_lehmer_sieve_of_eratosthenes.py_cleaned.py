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
def get_primes(start, end):
    prime_list = []
    for num in range(start, end):
        if is_prime(num):
            prime_list.append(num)
    return prime_list
def lucas_lehmer(p):
    lucas_lehmer_sequence = [4] * (p - 1)
    for i in range(1, p - 1):
        lucas_lehmer_sequence[i] = (((lucas_lehmer_sequence[i - 1]) ** 2) - 2) % ((2 ** p) - 1)
    return lucas_lehmer_sequence[p - 2] == 0
def sieve(n):
    bool_list = [False, False] + [True] * (n - 1)
    p = 2
    while p is not None:
        for i in range(2 * p, n + 1, p):
            bool_list[i] = False
        p = next((i for i in range(p + 1, n + 1) if bool_list[i]), None)
    return [i for i, prime in enumerate(bool_list) if prime]
print("Mersenne numbers:")
primes = get_primes(3, 65)
mersenne_list = [mersenne_number(prime) for prime in primes]
print(mersenne_list)
print(len(mersenne_list))
print("\nLucas-Lehmer test for primality:")
my_primes = get_primes(3, 65)
my_logic = [lucas_lehmer(idx) for idx in my_primes]
print(list(zip(my_primes, my_logic)))
print("\nSieve of Eratosthenes:")
print(sieve(1000))