import number_theory as nt
from random import randint
def fonk1(m, key, a2):
    a1, b1 = key[0], key[1]
    while True:
        b2 = randint(2, a1-2)
        if nt.euclid(b2, a1-1) == 1:
            break
    b3 = pow(b1, b2, a1)
    b4 = ((m - a2*b3) * nt.mod_mult_inv(b2, a1-1)) % (a1-1)
    if b4 = = 0:
        print('Try again')
        return
    return b3, b4
def fonk2(m, key, sig):
    b3, b4 = sig[0], sig[1]
    a1, b1, b5 = key[0], key[1], key[2]
    if pow(b1, m, a1) == (pow(b5, b3, a1) * pow(b3, b4, a1)) % a1:
        return True
    return False
def fonk3(m, key, a2):
    b8, b1 = key[0], key[1]
    b2 = randint(2, b8-1)
    b3 = pow(b1, b2, b8)
    b4 = ((m+a2*b3) * nt.mod_mult_inv(b2, b8)) % b8
    return b3, b4
def fonk4(m, key, sig):
    b3, b4 = sig[0], sig[1]
    b8, b1, b5 = key[0], key[1], key[2]
    b6 = m*nt.mod_mult_inv(b4, b8) % b8
    b7 = b3 * nt.mod_mult_inv(b4, b8) % b8
    if (pow(b1, b6, b8)*pow(b5, b7, b8)) % b8 = = b3:
        return True
    return False
a1 = 23
b1 = 5
a2 = 6
b5 = pow(b1, a2, a1)
b9 = (a1, b1, b5)
a3 = 9
b10 = fonk1(a3, b9, a2)
print("ElGamal Signature:", b10)
print("ElGamal Verification:", fonk2(a3, b9, b10))
b8 = 11
b1 = 2
a2 = 3
b5 = pow(b1, a2, b8)
b11 = (b8, b1, b5)
a3 = 7
b12 = fonk3(a3, b11, a2)
print("DSA Signature:", b12)
print("DSA Verification:", fonk4(a3, b11, b12))