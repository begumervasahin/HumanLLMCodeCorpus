import random
def modular_exp(a, b, n):
    result = 1
    while b > 0:
        if b & 1:
            result = (result * a) % n
        a = (a * a) % n
        b >>= 1
    return result
def gen_rand(bit_length):
    bits = [random.randint(0, 1) for _ in range(bit_length - 2)]
    num = 1
    for bit in bits:
        num = num * 2 + bit
    return num * 2 + 1
def miller_rabin_test(n, k=100):
    if n in (2, 3):
        return True
    if n % 2 == 0 or n == 1:
        return False
    d, s = n - 1, 0
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
        if miller_rabin_test(candidate):
            return candidate
def extended_gcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0
def gen_private_exponent(e, phi):
    _, x, _ = extended_gcd(e, phi)
    return x % phi
def lsb_leak_attack(e, n, c, oracle):
    low, high = 0.0, n
    i = 1
    while high - low >= 1:
        mid = (low + high) / 2
        if oracle(modular_exp(2, i * e, n) * c % n) == 0:
            high = mid
        else:
            low = mid
        i += 1
    return int(low)
if __name__ == '__main__':
    bit_length = 256
    p = gen_prime(bit_length)
    q = gen_prime(bit_length)
    n = p * q
    e = 65537
    phi = (p - 1) * (q - 1)
    d = gen_private_exponent(e, phi)
    print(f"p: {p}")
    print(f"q: {q}")
    print(f"e: {e}")
    print(f"d: {d}")
    print(f"n: {n}")
    print()
    plaintext = 123456789
    ciphertext = modular_exp(plaintext, e, n)
    decrypted_text = modular_exp(ciphertext, d, n)
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted text: {decrypted_text}")
    print()
    print("Performing LSB Leak Attack...")
    oracle = lambda x: modular_exp(x, d, n) % 2
    leaked_plaintext = lsb_leak_attack(e, n, ciphertext, oracle)
    print(f"Leaked plaintext: {leaked_plaintext}")
    print()