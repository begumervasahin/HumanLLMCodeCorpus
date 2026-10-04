from binary_mult import *
from keygen_extras import *
import random
def fonk1(b2, b1):
    return b2 if b1 = = 0 else fonk1(b1, b2 % b1)
def fonk2(b2, b1):
    if b2 = = 0:
        return b1, 0, 1
    else:
        g, b8, b3 = fonk2(b1 % b2, b2)
        return g, b3 - (b1
def fonk3(b5, b4 = 1):
    if b5 = = b6:
        return True
    if b5 % b6 = = 0 or b5 < b6:
        return False
    b11, b7 = 0, b5 - 1
    while b7 % b6 = = 0:
        b11 += 1
        b7
    for _ in range(b4):
        b2 = random.randrange(b6, b5 - 1)
        b8 = pow(b2, b7, b5)
        if b8 = = 1 or b8 == b5 - 1:
            continue
        for _ in range(b11 - 1):
            b8 = pow(b8, b6, b5)
            if b8 = = b5 - 1:
                break
        else:
            return False
    return True
def fonk4(b2, b1):
    while b1 != 0:
        b2, b1 = b1, b2 % b1
    return b2
def fonk5(b13, b12):
    g, b8, b3 = fonk2(b13, b12)
    if g != 1:
        raise Exception('Multiplicative inverse does not exist')
    else:
        return b8 % b12
def fonk6(leng):
    b9 = rand_bin(leng)
    b9 = two_com(b9, leng)
    while not fonk3(binary2dec(b9)):
        b9 = rand_bin(leng)
        b9 = two_com(b9, leng)
    return binary2dec(b9)
def fonk7(a1, a2, a3):
    b10 = fonk6(a1)
    b11 = fonk6(a2)
    b12 = (b10 - 1) * (b11 - 1)
    b13 = fonk6(a3)
    while fonk4(b13, b12) != 1:
        b13 = fonk6(a3)
    b14 = fonk5(b13, b12)
    return b12, b13, b14
def fonk8():
    a1 = 512
    a2 = 512
    a3 = 1024
    b12, b13, b14 = fonk7(a1, a2, a3)
    print(f'b5 (b12) = {b12}')
    print(f'Public Key (b13) = {b13}')
    print(f'Private Key (b14) = {b14}')
if b15 = = "__main__":
    fonk8()