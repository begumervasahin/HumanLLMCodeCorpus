import random
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def get_primes():
    primes = [i for i in range(2, 50) if is_prime(i)]
    return primes
def get_random_prime(primes):
    return random.choice(primes)
def get_phy_n():
    primes = get_primes()
    p = get_random_prime(primes)
    q = get_random_prime(primes)
    while p == q:
        q = get_random_prime(primes)
    n = p * q
    phy = (p - 1) * (q - 1)
    return phy, n
def get_d(e, phy):
    for d in range(1, phy):
        if (e * d) % phy == 1:
            return d
    return None
def get_e(phy):
    e = random.randint(2, phy - 1)
    while gcd(e, phy) != 1:
        e = random.randint(2, phy - 1)
    return e
def get_ascii(message):
    return [ord(char) for char in message]
def encrypt(ascii_codes, n, e):
    return [(code ** e) % n for code in ascii_codes]
def decrypt(crypted, n, d):
    return ''.join(chr((code ** d) % n) for code in crypted)
def main():
    phy, n = get_phy_n()
    e = get_e(phy)
    d = get_d(e, phy)
    message = input("Enter Your Message: ")
    ascii_codes = get_ascii(message)
    crypted = encrypt(ascii_codes, n, e)
    decrypted_message = decrypt(crypted, n, d)
    print("Encrypted message: ", crypted)
    print("Decrypted message: ", decrypted_message)
if __name__ == "__main__":
    main()