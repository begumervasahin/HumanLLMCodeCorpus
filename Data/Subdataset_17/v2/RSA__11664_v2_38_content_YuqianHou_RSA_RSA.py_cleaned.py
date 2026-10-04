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
    print(f'ç´ æ°çæçæ¶é´ä¸ºï¼ {end_time - start_time} s')
    print(f"n = p * q = {n}")
    print(f"å©ç¨Euclideanç®æ³çæçå
¬é¥ e = {e}")
    print(f"å©ç¨æ©å±Euclideanç®æ³çæçç§é¥ d = {d}")
    public_key = (n, e)
    private_key = (n, d)
    return public_key, private_key
def main():
    public_key, private_key = generate_rsa_key()
    print('è¯·è¾å
¥ææï¼')
    plaintext = int(input())
    ciphertext = encryption(plaintext, public_key)
    print(f"RSAå å¯åçå¯æä¸º: {ciphertext}")
    decrypted_text = decryption(ciphertext, private_key)
    print(f"RSAè§£å¯åçææä¸º: {decrypted_text}")
    if plaintext == decrypted_text:
        print('è§£å¯æå')
    total_encryption_time = 0
    total_decryption_time = 0
    for _ in range(10):
        print('è¯·è¾å
¥ææï¼')
        plaintext = int(input())
        start_time = time.perf_counter()
        ciphertext = encryption(plaintext, public_key)
        end_time = time.perf_counter()
        total_encryption_time += (end_time - start_time)
        print(f"RSAå å¯åçå¯æä¸º: {ciphertext}")
        start_time = time.perf_counter()
        decrypted_text = decryption(ciphertext, private_key)
        end_time = time.perf_counter()
        total_decryption_time += (end_time - start_time)
        print(f"RSAè§£å¯åçææä¸º: {decrypted_text}")
    print(f'10ç»ææçRSAå å¯æ¶é´ä¸ºï¼ {total_encryption_time}')
    print(f'10ç»ææçRSAè§£å¯æ¶é´ä¸ºï¼ {total_decryption_time}')
if __name__ == '__main__':
    main()