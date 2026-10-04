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
def get_primes(a, b):
    return [i for i in range(a, b) if is_prime(i)]
def lucas_lehmer(p):
    if p == 2:
        return True
    s = 4
    m = (2 ** p) - 1
    for _ in range(p - 2):
        s = (s * s - 2) % m
    return s == 0
def is_prime_fast(number):
    if number <= 1:
        return False
    if number % 2 == 0:
        return number == 2
    for factor in range(3, int(math.sqrt(number)) + 1, 2):
        if number % factor == 0:
            return False
    return True
def get_primes_fast(n):
    return [number for number in range(n) if is_prime_fast(number)]
def list_true(n):
    return [i >= 2 for i in range(n + 1)]
def mark_false(bool_list, p):
    for i in range(2 * p, len(bool_list), p):
        bool_list[i] = False
    return bool_list
def find_next(bool_list, p):
    for i in range(p + 1, len(bool_list)):
        if bool_list[i]:
            return i
    return None
def prime_from_list(bool_list):
    return [i for i, is_prime in enumerate(bool_list) if is_prime]
def sieve(n):
    bool_list = list_true(n)
    p = 2
    while p is not None:
        bool_list = mark_false(bool_list, p)
        p = find_next(bool_list, p)
    return prime_from_list(bool_list)
if __name__ == '__main__':
    primes = get_primes(3, 65)
    mersenne_list = [mersenne_number(prime) for prime in primes]
    print("Mersenne numbers:", mersenne_list)
    print("Count of Mersenne numbers:", len(mersenne_list))
    n_start = 3
    n_end = 65
    mersennes = [mersenne_number(number) for number in range(n_start, n_end) if is_prime(number)]
    print("Filtered Mersenne numbers:", mersennes)
    print("Count of filtered Mersenne numbers:", len(mersennes))
    print("Lucas-Lehmer test results:")
    test_primes = get_primes(3, 65)
    lucas_lehmer_results = [(prime, lucas_lehmer(prime)) for prime in test_primes]
    print(lucas_lehmer_results)
    print("Fast prime check results:")
    for n in range(10000):
        assert is_prime(n) == is_prime_fast(n)
    print("Get primes fast:", get_primes_fast(20))
    print("Sieve of Eratosthenes results match traditional prime list up to 1000:")
    assert sieve(1000) == get_primes(0, 1000)