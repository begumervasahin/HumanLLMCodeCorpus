import number_theory as nt
from random import randint
def elgamal_sign(m, key, x):
    p, g = key
    while True:
        k = randint(2, p - 2)
        if nt.euclid(k, p - 1) == 1:
            break
    s1 = pow(g, k, p)
    s2 = ((m - x * s1) * nt.mod_mult_inv(k, p - 1)) % (p - 1)
    if s2 == 0:
        print('Try again')
        return None
    return s1, s2
def elgamal_verify(m, key, sig):
    s1, s2 = sig
    p, g, y = key
    return pow(g, m, p) == (pow(y, s1, p) * pow(s1, s2, p)) % p
def dsa_sign(m, key, x):
    q, g = key
    k = randint(2, q - 1)
    s1 = pow(g, k, q)
    s2 = ((m + x * s1) * nt.mod_mult_inv(k, q)) % q
    return s1, s2
def dsa_verify(m, key, sig):
    s1, s2 = sig
    q, g, y = key
    v1 = (m * nt.mod_mult_inv(s2, q)) % q
    v2 = (s1 * nt.mod_mult_inv(s2, q)) % q
    return (pow(g, v1, q) * pow(y, v2, q)) % q == s1
if __name__ == "__main__":
    p = 23
    g = 5
    y = 8
    x = 6
    elgamal_key = (p, g)
    elgamal_pub_key = (p, g, y)
    message = 15
    elgamal_signature = elgamal_sign(message, elgamal_key, x)
    if elgamal_signature:
        print("ElGamal Signature:", elgamal_signature)
        is_valid = elgamal_verify(message, elgamal_pub_key, elgamal_signature)
        print("ElGamal Signature Valid:", is_valid)
    q = 23
    g = 5
    y = 8
    x = 6
    dsa_key = (q, g)
    dsa_pub_key = (q, g, y)
    dsa_signature = dsa_sign(message, dsa_key, x)
    print("DSA Signature:", dsa_signature)
    is_valid = dsa_verify(message, dsa_pub_key, dsa_signature)
    print("DSA Signature Valid:", is_valid)