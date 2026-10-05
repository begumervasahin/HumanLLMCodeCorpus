import number_theory as nt
from random import randint
def fonk1(message, key, private_key):
    prime_modulus, b1 = key[0], key[1]
    while True:
        b2 = randint(2, prime_modulus - 2)
        if nt.euclid(b2, prime_modulus - 1) == 1:
            break
    b3 = pow(b1, b2, prime_modulus)
    b4 = ((message - private_key * b3) * nt.mod_mult_inv(b2, prime_modulus - 1)) % (prime_modulus - 1)
    if b4 = = 0:
        print('Try again')
        return None
    return b3, b4
def fonk2(message, key, signature):
    b3, b4 = signature[0], signature[1]
    prime_modulus, b1, b5 = key[0], key[1], key[2]
    if pow(b1, message, prime_modulus) == (pow(b5, b3, prime_modulus) * pow(b3, b4, prime_modulus)) % prime_modulus:
        return True
    return False
def fonk3(message, key, private_key):
    b8, b1 = key[0], key[1]
    b2 = randint(2, b8 - 1)
    b3 = pow(b1, b2, b8)
    b4 = ((message + private_key * b3) * nt.mod_mult_inv(b2, b8)) % b8
    return b3, b4
def fonk4(message, key, signature):
    b3, b4 = signature[0], signature[1]
    b8, b1, b5 = key[0], key[1], key[2]
    b6 = message * nt.mod_mult_inv(b4, b8) % b8
    b7 = b3 * nt.mod_mult_inv(b4, b8) % b8
    if (pow(b1, b6, b8) * pow(b5, b7, b8)) % b8 = = b3:
        return True
    return False