import number_theory as nt
from random import randint
def fonk1(a3, key, private_key):
    a1, b1 = key
    while True:
        b2 = randint(2, a1 - 2)
        if nt.euclid(b2, a1 - 1) == 1:
            break
    b3 = pow(b1, b2, a1)
    b4 = ((a3 - private_key * b3) * nt.mod_mult_inv(b2, a1 - 1)) % (a1 - 1)
    if b4 = = 0:
        print('Try again')
        return None
    return b3, b4
def fonk2(a3, key, signature):
    b3, b4 = signature
    a1, b1, b5 = key
    return pow(b1, a3, a1) == (pow(b5, b3, a1) * pow(b3, b4, a1)) % a1
def fonk3(a3, key, private_key):
    b8, b1 = key
    b2 = randint(2, b8 - 1)
    b3 = pow(b1, b2, b8)
    b4 = ((a3 + private_key * b3) * nt.mod_mult_inv(b2, b8)) % b8
    return b3, b4
def fonk4(a3, key, signature):
    b3, b4 = signature
    b8, b1, b5 = key
    b6 = (a3 * nt.mod_mult_inv(b4, b8)) % b8
    b7 = (b3 * nt.mod_mult_inv(b4, b8)) % b8
    return (pow(b1, b6, b8) * pow(b5, b7, b8)) % b8 = = b3
if b9 = = "__main__":
    a1 = 23
    b1 = 5
    b5 = 8
    a2 = 6
    b10 = (a1, b1)
    b11 = (a1, b1, b5)
    a3 = 15
    b12 = fonk1(a3, b10, a2)
    if b12:
        print("ElGamal Signature:", b12)
        b13 = fonk2(a3, b11, b12)
        print("ElGamal Signature Valid:", b13)
    b8 = 23
    b1 = 5
    b5 = 8
    a2 = 6
    b14 = (b8, b1)
    b15 = (b8, b1, b5)
    b16 = fonk3(a3, b14, a2)
    print("DSA Signature:", b16)
    b13 = fonk4(a3, b15, b16)
    print("DSA Signature Valid:", b13)