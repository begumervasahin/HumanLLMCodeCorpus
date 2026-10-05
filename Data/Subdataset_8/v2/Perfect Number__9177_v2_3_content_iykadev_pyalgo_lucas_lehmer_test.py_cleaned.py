from sys import stdout
from math import sqrt, log
def is_prime(n):
    if n == 2:
        return True
    elif n <= 1 or n % 2 == 0:
        return False
    else:
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
def is_mersenne_prime(p):
    if p == 2:
        return True
    else:
        mersenne_number = (1 << p) - 1
        s = 4
        for i in range(3, p + 1):
            s = (s ** 2 - 2) % mersenne_number
        return s == 0
precision = 20000
long_bits_width = precision * log(10, 2)
upper_bound_prime = int(long_bits_width - 1) / 2
upper_bound_count = 45
print("Finding Mersenne primes in M[2..%d]:" % upper_bound_prime)
count = 0
for p in range(2, int(upper_bound_prime + 1)):
    if is_prime(p) and is_mersenne_prime(p):
        print("M%d" % p, end=" ")
        stdout.flush()
        count += 1
    if count >= upper_bound_count:
        break
print()