import random
import gmpy2
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def multiplicative_inverse(e, phi):
    r1 = phi
    r2 = e
    t1 = 0
    t2 = 1
    while r2 > 0:
        q = r1
        r = r1 % r2
        r1 = r2
        r2 = r
        t = t1 - q * t2
        t1 = t2
        t2 = t
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
    elif p == q:
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
def encrypt(pk, plaintext):
    key, n = pk
    cipher = [gmpy2.powmod(ord(char), key, n) for char in plaintext]
    return cipher
def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(gmpy2.powmod(char, key, n)) for char in ciphertext]
    return ''.join(plain)
if __name__ == '__main__':
    p = int(input("Enter a prime number p: "))
    q = int(input("Enter another prime number q (Different from above): "))
    public, private = generate_keypair(p, q)
    message = str(input("Enter a message to encrypt with the private key: "))
    print('\nPublic key: ', public)
    print('Private key: ', private)
    encrypted_msg = encrypt(private, message)
    print("\nEncrypted message: ")
    print(''.join(map(str, encrypted_msg)))
    decrypted_msg = decrypt(public, encrypted_msg)
    print("\nDecrypted message: ")
    print(decrypted_msg)