import random
import sys
def main():
    p = generate_prime(1, 2**8)
    q = generate_prime(1, 2**8)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = generate_coprime(phi)
    d = modular_inverse(e, phi)
    print(f"p = {p}\nq = {q}\nn = {n}\nphi = {phi}\ne = {e}\nd = {d}")
    if len(sys.argv) >= 3:
        choice = sys.argv[1]
        message = int(sys.argv[2])
        if choice in ("enc", "e"):
            print(f"Message = {message}\nEncrypted = {encrypt(message, e, n)}")
        elif choice in ("dec", "d"):
            print(f"Ciphertext = {message}\nDecrypted = {decrypt(message, d, n)}")
    else:
        print("Please provide arguments for encryption/decryption.")
def generate_prime(start, end):
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num
def generate_coprime(phi):
    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            return e
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def modular_inverse(e, phi):
    d = extended_gcd(e, phi)[1]
    return d % phi
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b
def encrypt(message, e, n):
    return pow(message, e, n)
def decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)
if __name__ == "__main__":
    main()