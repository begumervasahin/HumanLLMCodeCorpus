import random
def RSA(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    relative_primes = [e for e in range(2, phi) if math.gcd(e, phi) == 1]
    e = random.choice(relative_primes)
    d = pow(e, -1, phi)
    return relative_primes, phi, n, d, e
def encrypt(e, n, plaintext):
    return pow(plaintext, e, n)
def decrypt(d, n, ciphertext):
    return pow(ciphertext, d, n)
def main():
    p = 1733
    q = 1301
    relative_primes, phi, n, d, e = RSA(p, q)
    print(f"Relative Primes: {relative_primes}")
    print(f"phi: {phi}, n: {n}, d: {d}, e: {e}\n")
    payload = 2999
    print(f"Starting value: {payload}")
    encrypted_payload = encrypt(e, n, payload)
    print(f"Encrypted: {encrypted_payload}")
    decrypted_payload = decrypt(d, n, encrypted_payload)
    print(f"Decrypted: {decrypted_payload}")
if __name__ == "__main__":
    main()