import random
from random import randrange
def binary2dec(binary):
    return int(binary, 2)
def dec2binary(dec, length):
    return bin(dec)[2:].zfill(length)
def rand_bin(length):
    return ''.join([str(randrange(0, 2)) for _ in range(length)])
def two_complement(binary, length):
    if binary[0] == '1':
        complement = ''.join('1' if bit == '0' else '0' for bit in binary)
        return bin(binary2dec(complement) + 1)[2:].zfill(length)
    return binary.zfill(length)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = egcd(b % a, a)
        return g, y - (b
def multiplicative_inverse(e, phi):
    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception('No modular inverse')
    else:
        return x % phi
def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
def generate_prime(length):
    prime_candidate = rand_bin(length)
    prime_candidate = two_complement(prime_candidate, length)
    while not is_prime(binary2dec(prime_candidate)):
        prime_candidate = rand_bin(length)
        prime_candidate = two_complement(prime_candidate, length)
    return binary2dec(prime_candidate)
def main():
    bit_length = 512
    e_length = 1024
    p = generate_prime(bit_length)
    q = generate_prime(bit_length)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = generate_prime(e_length)
    while gcd(e, phi) != 1 or not is_prime(e):
        e = generate_prime(e_length)
    d = multiplicative_inverse(e, phi)
    print(f'n = {n}')
    print(f'Public Key (e) = {e}')
    print(f'Private Key (d) = {d}')
if __name__ == "__main__":
    main()