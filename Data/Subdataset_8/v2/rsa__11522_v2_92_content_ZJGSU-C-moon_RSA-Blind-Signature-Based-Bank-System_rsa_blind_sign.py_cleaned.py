import hashlib
import gmpy2
import random
import time
def get_prime(rs):
    p = gmpy2.mpz_urandomb(rs, 1024)
    while not gmpy2.is_prime(p):
        p += 1
    return p
def key_generation():
    rs = gmpy2.random_state(int(time.time()))
    p = get_prime(rs)
    q = get_prime(rs)
    n = p * q
    e = 0x10001
    H = lambda m: int(hashlib.sha256(m.encode()).hexdigest(), 16)
    public_key = [n, e, H]
    d = gmpy2.invert(e, (p - 1) * (q - 1))
    private_key = d
    return public_key, private_key
def sign_message(public_key, private_key, message):
    n = public_key[0]
    e = public_key[1]
    H = public_key[2]
    d = private_key
    R = random.randrange(0, n)
    H_m = H(message) % n
    R_e = gmpy2.powmod(R, e, n)
    M = R_e * H_m % n
    M_d = gmpy2.powmod(M, d, n)
    R_inv = gmpy2.invert(R, n)
    signature = gmpy2.mul(M_d, R_inv) % n
    return signature
def verify_signature(public_key, signature):
    n = public_key[0]
    e = public_key[1]
    verification_result = gmpy2.powmod(signature, e, n)
    return verification_result
if __name__ == '__main__':
    message = input('Please input your message: ')
    public_key, private_key = key_generation()
    signature = sign_message(public_key, private_key, message)
    print('Signature:', signature)
    verification_result = verify_signature(public_key, signature)
    print('Verification Result:', verification_result)