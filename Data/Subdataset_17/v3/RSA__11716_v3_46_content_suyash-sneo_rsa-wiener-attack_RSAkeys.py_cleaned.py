import random
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
def extended_euclid(a, b):
    x, last_x = 0, 1
    y, last_y = 1, 0
    while b:
        q = a
        a, b = b, a % b
        x, last_x = last_x - q * x, x
        y, last_y = last_y - q * y, y
    return last_x, last_y, a
def mod_inverse(n, e):
    inv, _, _ = extended_euclid(e, n)
    return inv % n
def int_sqrt(n):
    x = n
    y = (x + 1)
    while y < x:
        x = y
        y = (x + n
    return x if x * x == n else -1
def miller_rabin_test(a, s, d, n):
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(s - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    return False
def is_prime(n, k=20):
    if n in (2, 3):
        return True
    if n % 2 == 0 or n < 2:
        return False
    s, d = 0, n - 1
    while d % 2 == 0:
        d
        s += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        if not miller_rabin_test(a, s, d, n):
            return False
    return True
def generate_prime(nbits):
    while True:
        p = random.getrandbits(nbits)
        p |= (1 << nbits - 1) | 1
        if is_prime(p):
            return p
def generate_prime_in_range(start, stop):
    while True:
        p = random.randint(start, stop)
        p |= 1
        if is_prime(p):
            return p
def generate_pq(nbits=512):
    p = generate_prime(nbits)
    q = generate_prime_in_range(p + 1, 2 * p)
    return p, q
def generate_rsa_keys(nbits=1024):
    p, q = generate_pq(nbits
    N = p * q
    totient = (p - 1) * (q - 1)
    while True:
        d = random.getrandbits(nbits
        if gcd(d, totient) == 1 and 36 * pow(d, 4) < N:
            break
    e = mod_inverse(totient, d)
    return N, e, d
if __name__ == "__main__":
    nbits = 1024
    N, e, d = generate_rsa_keys(nbits)
    print(f"Public key (N, e): ({N}, {e})")
    print(f"Private key (N, d): ({N}, {d})")