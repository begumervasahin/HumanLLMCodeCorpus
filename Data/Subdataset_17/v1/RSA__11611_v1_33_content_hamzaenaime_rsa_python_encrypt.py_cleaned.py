import math
import random
import sys
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def is_prime(n):
    if n > 1:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return False
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
    phy = (p - 1) * (q - 1)
    return phy, n
def get_d(e, phy):
    for d in range(1, phy):
        if (e * d) % phy == 1:
            return d
def get_e(phy):
    while True:
        e = random.randint(2, phy - 1)
        if gcd(phy, e) == 1:
            return e
def get_ascii(message):
    return [ord(char) for char in message]
def crypter(code_ascii, N, E):
    n = int(N)
    e = int(E)
    crypted = [(char ** e) % n for char in code_ascii]
    return crypted
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <message>")
        sys.exit(1)
    msg = sys.argv[1]
    phy, n = get_phy_n()
    e = get_e(phy)
    d = get_d(e, phy)
    print(f"public key : ({n}, {e})")
    print(f"private key : ({n}, {d})")
    ascii_message = get_ascii(msg)
    encrypted_message = crypter(ascii_message, n, e)
    print(f"Encrypted message: {encrypted_message}")
    sys.stdout.flush()