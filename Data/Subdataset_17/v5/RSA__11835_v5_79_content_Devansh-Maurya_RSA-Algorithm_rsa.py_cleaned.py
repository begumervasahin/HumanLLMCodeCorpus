import random
import gmpy2
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def multiplicative_inverse(e, phi):
    r1, r2 = phi, e
    t1, t2 = 0, 1
    while r2 > 0:
        q = r1
        r1, r2 = r2, r1 % r2
        t1, t2 = t2, t1 - q * t2
    if r1 == 1:
        return t1 % phi
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5) + 2, 2):
        if num % n == 0:
            return False
    return True
def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    if p == q:
        raise ValueError('p and q cannot be equal')
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))
def encrypt(public_key, plaintext):
    key, n = public_key
    cipher = [gmpy2.powmod(ord(char), key, n) for char in plaintext]
    return cipher
def decrypt(private_key, ciphertext):
    key, n = private_key
    plain = [chr(gmpy2.powmod(char, key, n)) for char in ciphertext]
    return ''.join(plain)
if __name__ == '__main__':
    p = int(input("Enter a prime number p: "))
    q = int(input("Enter another prime number q (different from above): "))
    public_key, private_key = generate_keypair(p, q)
    message = input("Enter a message to encrypt with the private key: ")
    print('\nPublic key: ', public_key)
    print('Private key: ', private_key)
    encrypted_message = encrypt(private_key, message)
    print("\nEncrypted message: ")
    print(''.join(map(str, encrypted_message)))
    decrypted_message = decrypt(public_key, encrypted_message)
    print("\nDecrypted message: ")
    print(decrypted_message)