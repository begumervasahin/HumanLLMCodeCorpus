
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
    return [i for i in range(2, 50) if is_prime(i)]
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
    e = select_e(phi)
    d = calculate_d(e, phi)
    return n, e, d, phi
def select_e(phi):
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    return e
def calculate_d(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None
def convert_to_ascii(message):
    return [ord(char) for char in message]
def encrypt_message(ascii_codes, n, e):
    return [(code ** e) % n for code in ascii_codes]
def decrypt_message(encrypted_codes, n, d):
    return ''.join(chr((code ** d) % n) for code in encrypted_codes)
def main():
    n, e, d, _ = generate_keys()
    message = input("Enter Your Message: ")
    ascii_codes = convert_to_ascii(message)
    encrypted_codes = encrypt_message(ascii_codes, n, e)
    decrypted_message = decrypt_message(encrypted_codes, n, d)
    print("Encrypted message: ", encrypted_codes)
    print("Decrypted message: ", decrypted_message)
if __name__ == "__main__":
    main()