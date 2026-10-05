import hashlib
import gmpy2
import random
import time
def generate_prime(rs):
    p = gmpy2.mpz_urandomb(rs, 1024)
    while not gmpy2.is_prime(p):
        p += 1
    return p
def generate_keys():
    rs = gmpy2.random_state(int(time.time()))
    p = generate_prime(rs)
    q = generate_prime(rs)
    n = p * q
    e = 0x10001
    hash_function = lambda m: int(hashlib.sha256(m.encode()).hexdigest(), 16)
    public_key = {
        'n': n,
        'e': e,
        'hash_function': hash_function
    }
    d = gmpy2.invert(e, (p - 1) * (q - 1))
    private_key = d
    return public_key, private_key
def sign_message(public_key, private_key, message):
    n = public_key['n']
    e = public_key['e']
    hash_function = public_key['hash_function']
    d = private_key
    R = random.randrange(0, n)
    hashed_message = hash_function(message) % n
    R_e = gmpy2.powmod(R, e, n)
    M = R_e * hashed_message % n
    M_d = gmpy2.powmod(M, d, n)
    R_inv = gmpy2.invert(R, n)
    signature = gmpy2.mul(M_d, R_inv) % n
    return signature
def verify_signature(public_key, signature):
    n = public_key['n']
    e = public_key['e']
    verification_result = gmpy2.powmod(signature, e, n)
    return verification_result
if __name__ == '__main__':
    message = input('Please input your message: ')
    public_key, private_key = generate_keys()
    signature = sign_message(public_key, private_key, message)
    print('Signature:', signature)
    verification_result = verify_signature(public_key, signature)
    print('Verification Result:', verification_result)