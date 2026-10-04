import math
import random
import sys
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
    primes = [i for i in range(2, limit) if is_prime(i)]
    return primes
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
    e = generate_e(phi)
    d = generate_d(e, phi)
    return (e, n), (d, n)
def generate_d(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
def generate_e(phi):
    while True:
        e = random.randint(2, phi - 1)
        if gcd(phi, e) == 1:
            return e
def message_to_ascii(message):
    return [ord(char) for char in message]
def encrypt_message(ascii_message, n, e):
    return [(char ** e) % n for char in ascii_message]
def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <message>")
        sys.exit(1)
    message = sys.argv[1]
    public_key, private_key = generate_key_pair()
    e, n = public_key
    d, _ = private_key
    print(f"Public key : ({n}, {e})")
    print(f"Private key : ({n}, {d})")
    ascii_message = message_to_ascii(message)
    encrypted_message = encrypt_message(ascii_message, n, e)
    print(f"Encrypted message: {encrypted_message}")
    sys.stdout.flush()
if __name__ == "__main__":
    main()