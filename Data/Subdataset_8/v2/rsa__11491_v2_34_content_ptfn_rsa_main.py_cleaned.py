import random
import sys
def main():
    prime_numbers = generate_primes(1, 2**8)
    p = prime_numbers[random.randint(0, len(prime_numbers)-1)]
    q = prime_numbers[random.randint(0, len(prime_numbers)-1)]
    n = p * q
    phi = (p - 1) * (q - 1)
    e = prime_numbers[random.randint(0, len(prime_numbers)-1)]
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
def generate_primes(start, end):
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    return primes
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def modular_inverse(e, phi):
    for d in range(0, phi):
        if (e * d) % phi == 1:
            return d
def encrypt(message, e, n):
    return (message ** e) % n
def decrypt(ciphertext, d, n):
    return (ciphertext ** d) % n
if __name__ == "__main__":
    main()