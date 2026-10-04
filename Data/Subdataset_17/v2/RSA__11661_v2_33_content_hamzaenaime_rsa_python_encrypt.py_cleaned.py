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
def get_primes():
    primes = []
    for i in range(2, 50):
        if is_prime(i):
            primes.append(i)
    return primes
def get_random_prime():
    primes = get_primes()
    return random.choice(primes)
def get_phy_n():
    p = get_random_prime()
    q = get_random_prime()
    while p == q:
        q = get_random_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    return phi, n
def get_d(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
def get_e(phi):
    while True:
        e = random.randint(2, phi - 1)
        if gcd(phi, e) == 1:
            return e
def get_ascii(message):
    return [ord(char) for char in message]
def crypter(code_ascii, n, e):
    return [(char ** e) % n for char in code_ascii]
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <message>")
        sys.exit(1)
    msg = sys.argv[1]
    phi, n = get_phy_n()
    e = get_e(phi)
    d = get_d(e, phi)
    print(f"Public key : ({n}, {e})")
    print(f"Private key : ({n}, {d})")
    ascii_message = get_ascii(msg)
    encrypted_message = crypter(ascii_message, n, e)
    print(f"Encrypted message: {encrypted_message}")
    sys.stdout.flush()