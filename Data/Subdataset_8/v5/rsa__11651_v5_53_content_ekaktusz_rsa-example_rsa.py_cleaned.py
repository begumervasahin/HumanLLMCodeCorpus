import random
import decimal_string
import prime
def calculate_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def are_coprime(a, b):
    return calculate_gcd(a, b) == 1
def extended_euclidean_algorithm(a, b):
    x, y = a, b
    t0, t1 = 0, 1
    while y != 0:
        quotient = x
        remainder = x % y
        t = (t0 - quotient * t1) % a
        x, y = y, remainder
        t0, t1 = t1, t
    return t0
def generate_rsa_keys():
    prime_size = 512
    p, q = prime.generate_two_random_prime(prime_size)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(2, phi)
    while not are_coprime(e, phi):
        e = random.randrange(2, phi)
    d = extended_euclidean_algorithm(phi, e)
    return ((e, n), (d, n))
def rsa_encrypt(public_key, plaintext):
    e, n = public_key
    plaintext_number = decimal_string.text_to_integer(plaintext)
    ciphertext = pow(plaintext_number, e, n)
    return ciphertext
def rsa_decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext_number = pow(ciphertext, d, n)
    plaintext = decimal_string.integer_to_text(plaintext_number)
    return plaintext