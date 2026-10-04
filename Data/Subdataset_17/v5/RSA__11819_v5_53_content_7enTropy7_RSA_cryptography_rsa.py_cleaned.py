from math import sqrt
import sympy
import time
import binascii
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b
        m, n = x - u * q, y - v * q
        b, a = a, r
        x, y, u, v = u, v, m, n
    return b, x, y
def mod_inverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise ValueError("Modular inverse does not exist")
    return x % m
def generate_prime(bitlength):
    lower_bound = 1 << (bitlength - 1)
    upper_bound = (1 << bitlength) - 1
    return sympy.randprime(lower_bound, upper_bound)
def generate_keypair(keysize):
    p = generate_prime(keysize)
    q = generate_prime(keysize)
    print(f"Generated primes p: {p}, q: {q}")
    n = p * q
    phi = (p - 1) * (q - 1)
    e = sympy.randprime(1, phi)
    d = mod_inverse(e, phi)
    print(f"Generated public key (e, n): ({e}, {n})")
    print(f"Generated private key (d, n): ({d}, {n})")
    return (e, n), (d, n)
def encrypt(plain_text, public_key):
    e, n = public_key
    if plain_text > n:
        raise ValueError("Message is too large for the key to handle")
    return pow(plain_text, e, n)
def decrypt(ciphertext, private_key):
    d, n = private_key
    decrypted_msg = pow(ciphertext, d, n)
    return binascii.unhexlify(hex(decrypted_msg)[2:]).decode()
def main():
    public_key, private_key = generate_keypair(1024)
    msg = input("Write msg: ")
    hex_data = binascii.hexlify(msg.encode())
    plain_text = int(hex_data, 16)
    start_time = time.time()
    encrypted_msg = encrypt(plain_text, public_key)
    print(f"Encrypted message: {encrypted_msg}")
    decrypted_msg = decrypt(encrypted_msg, private_key)
    print(f"Decrypted message: {decrypted_msg}")
    print(f'Runtime: {time.time() - start_time} seconds')
if __name__ == "__main__":
    main()