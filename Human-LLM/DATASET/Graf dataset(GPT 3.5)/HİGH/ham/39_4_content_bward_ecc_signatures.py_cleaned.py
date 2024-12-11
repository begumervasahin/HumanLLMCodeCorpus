import number_theory as nt
from random import randint
def fonk1(m, key, x):
    p, b1 = key[0], key[1]
    while True:
        b2 = randint(2, p-2)
        if nt.euclid(b2, p-1) == 1:
            break
    b3 = pow(b1, b2, p)
    b4 = ((m - x*b3) * nt.mod_mult_inv(b2, p-1)) % (p-1)
    if b4 = = 0:
        print('Try again')
        return
    return b3, b4
def fonk2(m, key, sig):
    b3, b4 = sig[0], sig[1]
    p, b1, b5 = key[0], key[1], key[2]
    if pow(b1, m, p) == (pow(b5, b3, p) * pow(b3, b4, p)) % p:
        return True
    return False
def fonk3(m, key, x):
    b8, b1 = key[0], key[1]
    b2 = randint(2, b8-1)
    b3 = b1**b2 % b8
    b4 = ((m+x*b3) * nt.mod_mult_inv(b2, b8)) % b8
    return b3, b4
def fonk4(m, key, sig):
    b3, b4 = sig[0], sig[1]
    b8, b1, b5 = key[0], key[1], key[2]
    b6 = m*nt.mod_mult_inv(b4, b8) % b8
    b7 = b3 * nt.mod_mult_inv(b4, b8) % b8
    if (b1**b6*b5**b7) % b8 = = b3:
        return True
    return False