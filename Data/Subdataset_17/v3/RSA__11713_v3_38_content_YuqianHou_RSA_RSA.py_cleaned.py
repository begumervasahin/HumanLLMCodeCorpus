import random
import time
import Prime
def encryption(plaintext, public_key):
    n, e = public_key
    return Prime.quick_pow_mod(plaintext, e, n)
def decryption(ciphertext, private_key):
    n, d = private_key
    return Prime.quick_pow_mod(ciphertext, d, n)
def generate_rsa_key():
    start_time = time.perf_counter()
    p, q = Prime.get_rand_prime_arr(2)
    while p == q:
        q = random.choice(Prime.get_rand_prime_arr(2))
    end_time = time.perf_counter()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = Prime.mod_inverse(e, phi)
    print(f"éæºçæçç´ æ° p = {p}")
    print(f"éæºçæçç´ æ° q = {q}")
    print(f'ç´ æ°çæçæ¶é´ä¸ºï¼ {end_time - start_time:.6f} ç§')
    print(f"n = p * q = {n}")
    print(f"å©ç¨Euclideanç®æ³çæçå
¬é¥ e = {e}")
    print(f"å©ç¨æ©å±Euclideanç®æ³çæçç§é¥ d = {d}")
    return (n, e), (n, d)
def measure_time(func, *args):
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    return result, end_time - start_time
def main():
    public_key, private_key = generate_rsa_key()
    print('è¯·è¾å
¥ææï¼')
    plaintext = int(input())
    ciphertext, encryption_time = measure_time(encryption, plaintext, public_key)
    print(f"RSAå å¯åçå¯æä¸º: {ciphertext}")
    print(f"å å¯æ¶é´ä¸º: {encryption_time:.6f} ç§")
    decrypted_text, decryption_time = measure_time(decryption, ciphertext, private_key)
    print(f"RSAè§£å¯åçææä¸º: {decrypted_text}")
    print(f"è§£å¯æ¶é´ä¸º: {decryption_time:.6f} ç§")
    if plaintext == decrypted_text:
        print('è§£å¯æå')
    total_encryption_time = 0
    total_decryption_time = 0
    for _ in range(10):
        print('è¯·è¾å
¥ææï¼')
        plaintext = int(input())
        ciphertext, encryption_time = measure_time(encryption, plaintext, public_key)
        total_encryption_time += encryption_time
        print(f"RSAå å¯åçå¯æä¸º: {ciphertext}")
        decrypted_text, decryption_time = measure_time(decryption, ciphertext, private_key)
        total_decryption_time += decryption_time
        print(f"RSAè§£å¯åçææä¸º: {decrypted_text}")
    print(f'10ç»ææçRSAå å¯æ¶é´ä¸ºï¼ {total_encryption_time:.6f} ç§')
    print(f'10ç»ææçRSAè§£å¯æ¶é´ä¸ºï¼ {total_decryption_time:.6f} ç§')
if __name__ == '__main__':
    main()