import random
import math
def RSA(p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    relative_primes = []
    for e in range(2, phi_n):
        print("Working out the possible relative Primes...", int((e / phi_n) * 100), "%")
        if math.gcd(e, n) == 1 and math.gcd(e, p) == 1 and math.gcd(e, q) == 1 and math.gcd(e, phi_n) == 1:
            relative_primes.append(e)
    relative_primes.sort()
    d = False
    while not d:
        e = random.choice(relative_primes)
        d = d_check(e, phi_n)
    return relative_primes, phi_n, n, d, e
def d_check(e, phi_n):
    for d in range(1, phi_n):
        if (d * e) % phi_n == 1:
            return d
    return False
def encrypt(e, n, payload):
    return pow(payload, e, n)
def decrypt(d, n, payload):
    return pow(payload, d, n)
def main():
    p = 1733
    q = 1301
    relative_primes, phi_n, n, d, e = RSA(p, q)
    print(f"Relative Primes: {relative_primes}\nphi(n): {phi_n}\nn: {n}\nd: {d}\ne: {e}\n")
    payload = 2999
    print("Starting value:", payload)
    encrypted_payload = encrypt(e, n, payload)
    print("Encrypted:", encrypted_payload)
    decrypted_payload = decrypt(d, n, encrypted_payload)
    print("Decrypted:", decrypted_payload)
if __name__ == "__main__":
    main()