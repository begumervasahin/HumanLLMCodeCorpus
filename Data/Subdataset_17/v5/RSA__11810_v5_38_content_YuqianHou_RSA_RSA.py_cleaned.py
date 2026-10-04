import random
import time
import Prime
def encryption(plaintext, public_key):
    modulus, exponent = public_key
    return Prime.quick_pow_mod(plaintext, exponent, modulus)
def decryption(ciphertext, private_key):
    modulus, exponent = private_key
    return Prime.quick_pow_mod(ciphertext, exponent, modulus)
def generate_RSA_keys():
    start_time = time.perf_counter()
    prime_arr = Prime.get_rand_prime_arr(2)
    p, q = prime_arr
    while p == q:
        q = random.choice(prime_arr)
    end_time = time.perf_counter()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = Prime.mod_inverse(e, phi)
    print(f"Randomly generated prime p = {p}")
    print(f"Randomly generated prime q = {q}")
    print(f'Time taken to generate primes: {end_time - start_time} seconds')
    print(f"n = p * q = {n}")
    print(f"Public key exponent (e) = {e}")
    print(f"Private key exponent (d) = {d}")
    public_key = (n, e)
    private_key = (n, d)
    return public_key, private_key
if __name__ == '__main__':
    public_key, private_key = generate_RSA_keys()
    plaintext = int(input('Please enter plaintext: '))
    ciphertext = encryption(plaintext, public_key)
    print("Encrypted ciphertext:", ciphertext)
    decrypted_plaintext = decryption(ciphertext, private_key)
    print("Decrypted plaintext:", decrypted_plaintext)
    if plaintext == decrypted_plaintext:
        print('Decryption successful')
    total_encryption_time = 0
    total_decryption_time = 0
    for _ in range(10):
        plaintext = int(input('Please enter plaintext: '))
        start_time = time.perf_counter()
        ciphertext = encryption(plaintext, public_key)
        end_time = time.perf_counter()
        total_encryption_time += (end_time - start_time)
        print("Encrypted ciphertext:", ciphertext)
        start_time = time.perf_counter()
        decrypted_plaintext = decryption(ciphertext, private_key)
        end_time = time.perf_counter()
        total_decryption_time += (end_time - start_time)
        print("Decrypted plaintext:", decrypted_plaintext)
    print('Total encryption time for 10 messages:', total_encryption_time)
    print('Total decryption time for 10 messages:', total_decryption_time)