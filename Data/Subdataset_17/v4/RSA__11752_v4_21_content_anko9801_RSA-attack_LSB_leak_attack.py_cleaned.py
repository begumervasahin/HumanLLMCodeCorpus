import random
def modular_exp(a, b, n):
    res = 1
    while b > 0:
        if b & 1 == 1:
            res = (res * a) % n
        a = (a * a) % n
        b >>= 1
    return res
def gen_rand(bit_length):
    bits = [random.randint(0, 1) for _ in range(bit_length - 2)]
    ret = 1
    for b in bits:
        ret = ret * 2 + int(b)
    return ret * 2 + 1
def mr_primary_test(n, k=100):
    if n in (1, 2):
        return n == 2
    if n % 2 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d
        s += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = modular_exp(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = modular_exp(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
def gen_prime(bit_length):
    while True:
        candidate = gen_rand(bit_length)
        if mr_primary_test(candidate):
            return candidate
def exgcd(x, y):
    c0, c1 = x, y
    a0, a1 = 1, 0
    b0, b1 = 0, 1
    while c1 != 0:
        m = c0 % c1
        q = c0
        c0, c1 = c1, m
        a0, a1 = a1, a0 - q * a1
        b0, b1 = b1, b0 - q * b1
    return c0, a0, b0
def gen_d(e, phi):
    _, x, _ = exgcd(e, phi)
    return x % phi
def LSBLeakAttack(e, n, c, oracle):
    l, r = 0.0, n
    i = 1
    while r - l >= 1:
        m = (l + r) / 2
        if oracle(modular_exp(2, i * e, n) * c % n) == 0:
            r = m
        else:
            l = m
        i += 1
    return int(l)
if __name__ == '__main__':
    bits = 256
    p = gen_prime(bits)
    q = gen_prime(bits)
    e = 65537
    phi = (p - 1) * (q - 1)
    d = gen_d(e, phi)
    n = p * q
    print("p:", p)
    print("q:", q)
    print("e:", e)
    print("d:", d)
    print("n:", n)
    print()
    m = 123456789
    c = modular_exp(m, e, n)
    decrypted_m = modular_exp(c, d, n)
    print("Clear text:", m)
    print("Encrypted text:", c)
    print("Decrypted text:", decrypted_m)
    print()
    print("LSB Leak Attack")
    oracle = lambda x: modular_exp(x, d, n) % 2
    leaked_m = LSBLeakAttack(e, n, c, oracle)
    print("Leaked clear text:", leaked_m)
    print()