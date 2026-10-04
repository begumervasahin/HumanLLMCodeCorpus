import random
import math
def rsa_keygen(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    relative_primes = [e for e in range(2, phi) if math.gcd(e, phi) == 1]
    e = random.choice(relative_primes)
    d = pow(e, -1, phi)
    return relative_primes, phi, n, d, e
def encrypt(public_exponent, modulus, plaintext):
    return pow(plaintext, public_exponent, modulus)
def decrypt(private_exponent, modulus, ciphertext):
    return pow(ciphertext, private_exponent, modulus)
def main():
    p = 1733
    q = 1301
    relative_primes, phi, n, d, e = rsa_keygen(p, q)
    print(f"Relative Primes: {relative_primes}")
    print(f"phi (Euler's Totient): {phi}")
    print(f"Modulus (n): {n}")
    print(f"Private Exponent (d): {d}")
    print(f"Public Exponent (e): {e}\n")
    plaintext = 2999
    print(f"Starting value: {plaintext}")
    ciphertext = encrypt(e, n, plaintext)
    print(f"Encrypted: {ciphertext}")
    decrypted_plaintext = decrypt(d, n, ciphertext)
    print(f"Decrypted: {decrypted_plaintext}")
if __name__ == "__main__":
    main()