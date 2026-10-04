import math
from Crypto.Util import number
import os
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def ext_euclid(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, gcd = ext_euclid(b, a % b)
        return y, x - (a
def generate_keys(p, q):
    N = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    if gcd(e, phi) != 1:
        raise ValueError("Chosen e is not coprime with phi, try a different e")
    d = ext_euclid(e, phi)[0]
    d = d % phi
    if d < 0:
        d += phi
    return N, e, d
def fast_exp_mod(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp
    return result
def encrypt(message, e, N):
    print("[*] Encrypting...")
    return fast_exp_mod(message, e, N)
def decrypt(cipher, d, N):
    print("[*] Decrypting...")
    return fast_exp_mod(cipher, d, N)
def text_to_num(text):
    return int.from_bytes(text.encode(), 'big')
def num_to_text(num):
    return num.to_bytes((num.bit_length() + 7)
def RSA(message):
    m = text_to_num(message)
    print('[*] Message as number:', m)
    p = number.getPrime(256, os.urandom)
    print("[*] Prime p:", p)
    q = number.getPrime(256, os.urandom)
    print("[*] Prime q:", q)
    N, e, d = generate_keys(p, q)
    print("[*] RSA parameters N:", N, "e:", e, "d:", d)
    cipher = encrypt(m, e, N)
    print("[*] Encrypted message as number:", cipher)
    decrypted_message = decrypt(cipher, d, N)
    result = num_to_text(decrypted_message)
    print("[*] Decrypted message:", result)
if __name__ == "__main__":
    message = "Hi, this is RSA!"
    RSA(message)