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
def get_primes(limit=50):
    return [i for i in range(2, limit) if is_prime(i)]
def get_random_prime(primes):
    return random.choice(primes)
def generate_keys():
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
def generate_e(phi):
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    return e
def generate_d(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None
def get_ascii_codes(message):
    return [ord(char) for char in message]
def encrypt(ascii_codes, n, e):
    return [(code ** e) % n for code in ascii_codes]
def decrypt(crypted, n, d):
    return ''.join(chr((code ** d) % n) for code in crypted)
def main():
    public_key, private_key = generate_keys()
    e, n = public_key
    d, n = private_key
    message = input("Enter Your Message: ")
    ascii_codes = get_ascii_codes(message)
    encrypted_message = encrypt(ascii_codes, n, e)
    decrypted_message = decrypt(encrypted_message, n, d)
    print("Encrypted message: ", encrypted_message)
    print("Decrypted message: ", decrypted_message)
if __name__ == "__main__":
    main()