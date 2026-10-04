from binary_mult import *
from keygen_extras import *
import random
def fonk1(b2, b1):
    return b2 if b1 = = 0 else fonk1(b1, b2 % b1)
def fonk2(b2, b1):
    if b2 = = 0:
        return b1, 0, 1
    else:
        a5, b8, b3 = fonk2(b1 % b2, b2)
        return a5, b3 - (b1
def fonk3(b5, b4 = 1):
    if b5 = = b6:
        return True
    if b5 % b6 = = 0 or b5 < b6:
        return False
    b10, b7 = 0, b5 - 1
    while b7 % b6 = = 0:
        b10 += 1
        b7
    for _ in range(b4):
        b2 = random.randrange(b6, b5 - 1)
        b8 = pow(b2, b7, b5)
        if b8 = = 1 or b8 == b5 - 1:
            continue
        for _ in range(b10 - 1):
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
def fonk5(b11, b14):
    a5, b8, b3 = fonk2(b11, b14)
    if a5 != 1:
        raise Exception('Multiplicative inverse does not exist')
    else:
        return b8 % b14
def fonk6():
    a1 = 512
    a2 = 512
    a3 = 512
    a4 = 1024
    b9 = rand_bin(a3)
    b9 = two_com(b9, a1)
    while not fonk3(binary2dec(b9)):
        b9 = rand_bin(a3)
        b9 = two_com(b9, a3)
    b10 = rand_bin(a3)
    b10 = two_com(b10, a3)
    while not fonk3(binary2dec(b10)):
        b10 = rand_bin(a3)
        b10 = two_com(b10, a4)
    b11 = rand_bin(a4)
    b11 = two_com(b11, a4)
    b12 = binary2dec(b9)
    b13 = binary2dec(b10)
    b14 = (b12 - 1) * (b13 - 1)
    a5 = 5
    b15 = binary2dec(b11)
    while a5 != 1:
        while not fonk3(b15):
            b11 = rand_bin(a4)
            b11 = two_com(b11, a4)
            b15 = binary2dec(b11)
        a5 = fonk4(b15, b14)
    print('b5 b16 = ' + str(b14))
    print('')
    print('Public Key b16 = ' + str(b15))
    print('')
    b17 = fonk5(b15, b14)
    print('Private Key b16 = ' + str(b17))
    print('')
if b18 = = "__main__":
    fonk6()