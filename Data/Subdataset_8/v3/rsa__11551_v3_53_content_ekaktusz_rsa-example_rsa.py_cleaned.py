import random
import decimal_string
import prime
def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def are_coprime(a, b):
    return greatest_common_divisor(a, b) == 1
def extended_euclidean_algorithm(a, b):
    x, y = a, b
    t0, t1 = 0, 1
    r, t = b, 1
    while (x % y) != 0:
        q = x
        r = x % y
        t = (t0 - q * t1) % a
        x = y
        y = r
        t0 = t1
        t1 = t
    return t
def generate_rsa_keys():
    p, q = prime.generate_two_random_prime(512)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    while not are_coprime(e, phi):
        e = random.randrange(1, phi)
    d = extended_euclidean_algorithm(phi, e)
    return ((e, n), (d, n))
def encrypt_message(public_key, message):
    e, n = public_key
    message_number = decimal_string.text_to_integer(message)
    encrypted_message = pow(message_number, e, n)
    return encrypted_message
def decrypt_message(private_key, encrypted_message):
    d, n = private_key
    decrypted_message_number = pow(encrypted_message, d, n)
    decrypted_message = decimal_string.integer_to_text(decrypted_message_number)
    return decrypted_message
public_key, private_key = generate_rsa_keys()
message = "Hello, World!"
encrypted_message = encrypt_message(public_key, message)
print("Encrypted message:", encrypted_message)
decrypted_message = decrypt_message(private_key, encrypted_message)
print("Decrypted message:", decrypted_message)