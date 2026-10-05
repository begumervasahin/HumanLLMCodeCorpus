import number_theory as nt
from random import randint
def elgamal_sign(message, key, private_key):
    prime_modulus, generator = key[0], key[1]
    while True:
        k = randint(2, prime_modulus - 2)
        if nt.euclid(k, prime_modulus - 1) == 1:
            break
    s_1 = pow(generator, k, prime_modulus)
    s_2 = ((message - private_key * s_1) * nt.mod_mult_inv(k, prime_modulus - 1)) % (prime_modulus - 1)
    if s_2 == 0:
        print('Try again')
        return None
    return s_1, s_2
def elgamal_verify(message, key, signature):
    s_1, s_2 = signature[0], signature[1]
    prime_modulus, generator, public_key = key[0], key[1], key[2]
    if pow(generator, message, prime_modulus) == (pow(public_key, s_1, prime_modulus) * pow(s_1, s_2, prime_modulus)) % prime_modulus:
        return True
    return False
def dsa_sign(message, key, private_key):
    prime_order, generator = key[0], key[1]
    k = randint(2, prime_order - 1)
    s_1 = pow(generator, k, prime_order)
    s_2 = ((message + private_key * s_1) * nt.mod_mult_inv(k, prime_order)) % prime_order
    return s_1, s_2
def dsa_verify(message, key, signature):
    s_1, s_2 = signature[0], signature[1]
    prime_order, generator, public_key = key[0], key[1], key[2]
    v_1 = message * nt.mod_mult_inv(s_2, prime_order) % prime_order
    v_2 = s_1 * nt.mod_mult_inv(s_2, prime_order) % prime_order
    if (pow(generator, v_1, prime_order) * pow(public_key, v_2, prime_order)) % prime_order == s_1:
        return True
    return False