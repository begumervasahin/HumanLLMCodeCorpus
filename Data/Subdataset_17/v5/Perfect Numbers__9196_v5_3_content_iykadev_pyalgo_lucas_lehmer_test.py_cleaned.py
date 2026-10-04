import sys
from math import sqrt, log
def is_prime(p):
    if p == 2:
        return True
    if p <= 1 or p % 2 == 0:
        return False
    for i in range(3, int(sqrt(p)) + 1, 2):
        if p % i == 0:
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
def find_mersenne_primes(upper_bound_prime, upper_bound_count):
    print(f"Finding Mersenne primes in M[2..{upper_bound_prime}]:")
    count = 0
    for p in range(2, upper_bound_prime + 1):
        if is_prime(p) and is_mersenne_prime(p):
            print(f"M{p}", end=' ')
            sys.stdout.flush()
            count += 1
        if count >= upper_bound_count:
            break
    print()
def main():
    precision = 20000
    long_bits_width = precision * log(10, 2)
    upper_bound_prime = int(long_bits_width - 1)
    upper_bound_count = 45
    find_mersenne_primes(upper_bound_prime, upper_bound_count)
if __name__ == '__main__':
    main()