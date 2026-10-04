import random
def modular_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result
def generate_random(bit_length):
    bits = [random.randint(0, 1) for _ in range(bit_length - 2)]
    result = 1
    for bit in bits:
        result = result * 2 + bit
    return result * 2 + 1
def is_prime(n, k=100):
    if n in (2, 3):
        return True
    if n == 1 or n % 2 == 0:
        return False
    def decompose(n):
        exponent = 0
        while n % 2 == 0:
            n
            exponent += 1
        return n, exponent
    def check_composite(base, n, d, s):
        if modular_exp(base, d, n) == 1:
            return False
        for i in range(s):
            if modular_exp(base, d * (2 ** i), n) == n - 1:
                return False
        return True
    d, s = decompose(n - 1)
    for _ in range(k):
        base = random.randint(2, n - 2)
        if check_composite(base, n, d, s):
            return False
    return True
def generate_prime(bit_length):
    while True:
        candidate = generate_random(bit_length)
        if is_prime(candidate):
            return candidate
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        quotient = old_r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s, old_t
def mod_inverse(e, phi):
    gcd, x, _ = extended_gcd(e, phi)
    return x % phi
def pollards_rho(n):
    def f(x):
        return (x * x + 1) % n
    x, y, d = 2, 2, 1
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
    return d
def simple_attack(n, e, c):
    p = pollards_rho(n)
    q = n
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
    return p, q, d
if __name__ == '__main__':
    e = 65537
    m = 123456789
    bit_length = 10
    p = generate_prime(bit_length)
    q = generate_prime(bit_length)
    n = p * q
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
    c = modular_exp(m, e, n)
    print("Initial values:")
    print("e:", e)
    print("n:", n)
    p, q, d = simple_attack(n, e, c)
    print("Simple attack results:")
    print("Primes:", p, q)
    print("Decryption exponent:", d)