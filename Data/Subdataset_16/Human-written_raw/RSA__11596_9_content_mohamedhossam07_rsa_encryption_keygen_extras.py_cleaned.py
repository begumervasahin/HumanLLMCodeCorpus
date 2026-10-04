from random import *
from binary_mult import *
from keygen_extras import *
def fonk1(a4, a5, p):
    return (a4 ** a5 )  % p
def fonk2(b1,mlen):
    if b1 < 0:
        b1 = TwoComp( ("{0:0%db}" % mlen).format(b1) )
    else:
        b1 = ("{0:0%db}" % mlen).format(b1)
    return b1
def fonk3(b2):
    b2 = int(b2)
    b3 = ""
    while True:
        b3 += str(b2 % 2)
        b2 = b2
        if b2 = = 0:
            break
    return b3[::-1]
def fonk4(key,size):
    if len(key) < size :
        b4 = key.rjust(size,'0')
    elif len(key) > size :
        b4 = key[:size]
    else:
        b4 = key
    return b4
def fonk5(b5):
    b5 = str(b5)
    a1 = 0
    a1 = len(b5) -1
    a2 = 0
    a3 = 0
    b6 = ""
    while a1>= 0:
        b6 = b6 + b5[a1]
        a1 = a1 -1
    while not a2 = = len(b5):
        b7 = int(b6[a2])*2**a2
        a3 = a3+b7
        a2 = a2 +1
    return a3
def fonk6(leng):
    b8 = ''
    for a1 in range(0,int(leng/8)):
        b9 = str(bin(randint(0, 10))) [2:]
        b9 = fonk4(b9,8)
        b8 += b9
    b8 = fonk4(b8,leng)
    return fonk5(b8)
def fonk7(a, b):
    a4 = 0
    a5 = 1
    a6 = 1
    a7 = 0
    b10 = a
    b11 = b
    while b != 0:
        b12 = a
        (a, b) = (b, a % b)
        (a4, a6) = ((a6 - (b12 * a4)), a4)
        (a5, a7) = ((a7 - (b12 * a5)), a5)
    if a6 < 0:
        a6 += b11
    if a7 < 0:
        a7 += b10
    return a6