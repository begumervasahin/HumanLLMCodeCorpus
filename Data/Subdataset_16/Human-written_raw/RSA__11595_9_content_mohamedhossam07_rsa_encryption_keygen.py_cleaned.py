from binary_mult import *
from keygen_extras import *
from random import *
import random
def fonk1(b8,b1):
    if(b1 = =0):
        return b8
    else:
        return fonk1(b1,b8%b1)
def fonk2():
    a1 = 512
    a2 = 512
    a3 = 512
    a4 = 1024
    b2 = rand_bin(a3)
    b2 = two_com(b2,a1)
    while fonk4(binary2dec(b2) ) != True :
        b2 = rand_bin(a3)
        b2 = two_com(b2,a3)
    b3 = rand_bin(a3)
    b3 = two_com(b3,a3)
    while fonk4(binary2dec(b3)) != True :
        b3 = rand_bin(a3)
        b3 = two_com(b3,a4)
    b4 = rand_bin(a4)
    b4 = two_com(b4,a4)
    b2 = binary2dec(b2)
    b3 = binary2dec(b3)
    b5 = (b2-1)*(b3-1)
    a5 = 5
    b4 = binary2dec(b4)
    while a5 != 1:
        while fonk4(b4) != True :
            b4 = rand_bin(a4)
            b4 = two_com(b4,a4)
            b4 = binary2dec(b4)
        a5 = fonk5(b4, b5)
    print('b11 b6 = '+str(b5))
    print('')
    print('Public Key b6 = '+str(b4))
    print('')
    b7 = multiplicative_inverse(b4, b5)
    print('Private Key b6 = '+str(b7))
    print('')
def fonk3(b8, b1):
    if b8 = = 0:
        return (b1, 0, 1)
    else:
        a5, b14, b9 = fonk3(b1 % b8, b8)
        return (a5, b9 - (b1
def fonk4(b11, b10 = 1):
    if b11 = = b12:
        return True
    if b11 % b12 = = 0:
        return False
    b3, b13 = 0, b11 - 1
    while b13 % b12 = = 0:
        b3 += 1
        b13
    for _ in range(0,b10):
        b8 = random.randrange(b12, b11 - 1)
        b14 = pow(b8, b13, b11)
        if b14 = = 1 or b14 == b11 - 1:
            continue
        for _ in range(0,b3 - 1):
            b14 = power(b14, b12, b11)
            if b14 = = b11 - 1:
                break
        else:
            return False
    return True
def fonk5(b8, b1):
    while b1 != 0:
        b8, b1 = b1, b8 % b1
    return b8
if b15 = = "__main__":
    fonk2()