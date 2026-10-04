import random
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def extended_euclid(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return x0, y0, a
def mod_inverse(a, m):
    x, _, g = extended_euclid(a, m)
    if g != 1:
        raise ValueError('Modular inverse does not exist')
    return x % m
def integer_sqrt(n):
    x = n
    y = (x + 1)
    while y < x:
        x = y
        y = (x + n
    return x
def miller_rabin_test(a, d, n, s):
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(s - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    return False
def is_probably_prime(n, k=20):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    d, s = n - 1, 0
    while d % 2 == 0:
        d
        s += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        if not miller_rabin_test(a, d, n, s):
            return False
    return True
def generate_prime(nbits):
    while True:
        p = random.getrandbits(nbits) | (1 << (nbits - 1)) | 1
        if is_probably_prime(p):
            return p
def generate_prime_in_range(start, stop):
    while True:
        p = random.randint(start, stop - 1) | 1
        if is_probably_prime(p):
            return p
def generate_pq(nbits=512):
    p = generate_prime(nbits)
    q = generate_prime_in_range(p + 1, 2 * p)
    return p, q
def generate_rsa_keys(nbits=1024):
    p, q = generate_pq(nbits
    N = p * q
    phi = (p - 1) * (q - 1)
    while True:
        d = random.getrandbits(nbits
        if gcd(d, phi) == 1 and 36 * pow(d, 4) < N:
            break
    e = mod_inverse(d, phi)
    return N, e, d