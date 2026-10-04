import sys
from math import sqrt, log
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
def is_mersenne_prime(p):
    if p == 2:
        return True
    m_p = (1 << p) - 1
    s = 4
    for _ in range(3, p + 1):
        s = (s ** 2 - 2) % m_p
    return s == 0
def find_mersenne_primes(limit, max_count):
    count = 0
    for p in range(2, limit + 1):
        if is_prime(p) and is_mersenne_prime(p):
            print(f"M{p}", end=" ", flush=True)
            count += 1
        if count >= max_count:
            break
    print()
def main():
    precision = 20000
    long_bits_width = precision * log(10, 2)
    upper_bound_prime = int((long_bits_width - 1) / 2)
    upper_bound_count = 45
    print(f"Finding Mersenne primes in M[2..{upper_bound_prime}]:")
    find_mersenne_primes(upper_bound_prime, upper_bound_count)
if __name__ == '__main__':
    main()