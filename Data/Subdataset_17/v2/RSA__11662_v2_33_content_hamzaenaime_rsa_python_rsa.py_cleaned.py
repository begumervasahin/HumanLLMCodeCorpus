import math
import random
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def get_primes(limit=50):
    return [i for i in range(2, limit) if is_prime(i)]
def get_random_prime(primes):
    return random.choice(primes)
def generate_key_pair():
    primes = get_primes()
    p = get_random_prime(primes)
    q = get_random_prime(primes)
    while p == q:
        q = get_random_prime(primes)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = get_e(phi)
    d = get_d(e, phi)
    return e, d, n
def get_d(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
def get_e(phi):
    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            return e
def get_ascii_codes(message):
    return [ord(char) for char in message]
def encrypt(ascii_codes, n, e):
    encrypted = [(char ** e) % n for char in ascii_codes]
    encrypted_message = ''.join(map(str, encrypted))
    print("Encrypted message: " + encrypted_message)
    return encrypted
def decrypt(encrypted, n, d):
    decrypted = ''.join([chr((char ** d) % n) for char in encrypted])
    print("Decrypted message: " + decrypted)
    return decrypted
def main():
    e, d, n = generate_key_pair()
    message = input("Enter your message: ")
    ascii_codes = get_ascii_codes(message)
    encrypted = encrypt(ascii_codes, n, e)
    decrypt(encrypted, n, d)
if __name__ == "__main__":
    main()