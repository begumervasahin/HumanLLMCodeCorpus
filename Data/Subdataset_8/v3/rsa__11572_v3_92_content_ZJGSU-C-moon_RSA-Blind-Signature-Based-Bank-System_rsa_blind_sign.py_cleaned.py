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
    hash_func = lambda m: int(hashlib.sha256(m).hexdigest(), 16)
    public_key = [n, e, hash_func]
    d = gmpy2.invert(e, (p - 1) * (q - 1))
    private_key = d
    return public_key, private_key
def sign_message(public_key, private_key, message):
    n, e, hash_func = public_key
    d = private_key
    R = random.randrange(0, n)
    hash_message = hash_func(message) % n
    R_e = gmpy2.powmod(R, e, n)
    M = R_e * hash_message % n
    M_d = gmpy2.powmod(M, d, n)
    R_inverse = gmpy2.invert(R, n)
    signature = gmpy2.mul(M_d, R_inverse) % n
    return signature
def verify_signature(public_key, signature):
    n, e, _ = public_key
    verification = gmpy2.powmod(signature, e, n)
    return verification
if __name__ == '__main__':
    message = raw_input('Please input your message:')
    public_key, private_key = generate_keys()
    signature = sign_message(public_key, private_key, message)
    print 'Signature:', signature
    verification = verify_signature(public_key, signature)
    print 'Verification result:', verification