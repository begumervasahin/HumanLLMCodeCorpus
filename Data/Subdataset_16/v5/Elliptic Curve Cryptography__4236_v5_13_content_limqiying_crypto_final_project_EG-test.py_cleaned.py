from ecc_simple import *
import random
def fonk1(a4, b11, b8, b7):
    b1 = times(b8, b11)
    b2 = times(b8, b7)
    b3 = add(encode(a4, 100), b1)
    return b2, b3
def fonk2(b12, b9):
    b2, b3 = b12
    b4 = times(b9, b2)
    b5 = subtract(b3, b4)
    b6 = decode(b5, 100)
    return b6
def fonk3():
    set_p256_param()
    a1 = 115792089210356248762697446949407573530086143415290314195533631308867097853951
    a2 = 48439561293906451759052585252797914202762949526041747995844080717082404635286
    a3 = 36134250956749795798585127919587881956611106672985015071877198253568414405109
    b7 = (a2, a3)
    b8 = random.randrange(1, a1)
    b9 = random.randrange(1, a1)
    b10 = times(b8, b7)
    b11 = times(b9, b7)
    a4 = 32454324564335645345643
    b12 = fonk1(a4, b11, b8, b7)
    b6 = fonk2(b12, b9)
    print("Decrypted a4:", b6)
if b13 = = "__main__":
    fonk3()