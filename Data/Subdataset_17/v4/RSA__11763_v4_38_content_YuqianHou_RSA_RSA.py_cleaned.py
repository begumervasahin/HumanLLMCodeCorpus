import random
import time
import Prime
def encryption(plaintext, puk):
    return Prime.quick_pow_mod(plaintext, puk[1], puk[0])
def decryption(ciphertext, prk):
    return Prime.quick_pow_mod(ciphertext, prk[1], prk[0])
def get_RSAKey():
    RSAKey = {}
    start = time.perf_counter()
    prime_arr = Prime.get_rand_prime_arr(2)
    p, q = prime_arr[0], prime_arr[1]
    while p == q:
        q = random.choice(prime_arr)
    end = time.perf_counter()
    n = p * q
    s = (p - 1) * (q - 1)
    a = 65537
    b = Prime.mod_inverse(a, s)
    print("Randomly generated prime p =", p)
    print("Randomly generated prime q =", q)
    print('Time taken to generate primes:', end - start, 'seconds')
    print("n = p * q =", n)
    print("Public key exponent (a) =", a)
    print("Private key exponent (b) =", b)
    puk = [n, a]
    prk = [n, b]
    RSAKey['puk'] = puk
    RSAKey['prk'] = prk
    return RSAKey
if __name__ == '__main__':
    RSAKey = get_RSAKey()
    plaintext = int(input('Please enter plaintext: '))
    ciphertext = encryption(plaintext, RSAKey['puk'])
    print("Encrypted ciphertext:", ciphertext)
    decrypted_plaintext = decryption(ciphertext, RSAKey['prk'])
    print("Decrypted plaintext:", decrypted_plaintext)
    if plaintext == decrypted_plaintext:
        print('Decryption successful')
    total_encryption_time = 0
    total_decryption_time = 0
    for _ in range(10):
        plaintext = int(input('Please enter plaintext: '))
        start = time.perf_counter()
        ciphertext = encryption(plaintext, RSAKey['puk'])
        end = time.perf_counter()
        total_encryption_time += (end - start)
        print("Encrypted ciphertext:", ciphertext)
        start = time.perf_counter()
        decrypted_plaintext = decryption(ciphertext, RSAKey['prk'])
        end = time.perf_counter()
        total_decryption_time += (end - start)
        print("Decrypted plaintext:", decrypted_plaintext)
    print('Total encryption time for 10 messages:', total_encryption_time)
    print('Total decryption time for 10 messages:', total_decryption_time)