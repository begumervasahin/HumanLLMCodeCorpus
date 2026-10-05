
from ecc_simple import set_p256_param, times, add, subtract, encode, decode
import random
def fonk1():
    b1 = random.randrange(1, a1)
    b2 = times(b1, b3)
    return b1, b2
set_p256_param()
a1 = 115792089210356248762697446949407573530086143415290314195533631308867097853951
a2 = 48439561293906451759052585252797914202762949526041747995844080717082404635286
a3 = 36134250956749795798585127919587881956611106672985015071877198253568414405109
b3 = (a2, a3)
private_key_Alice, b4 = fonk1()
private_key_Bob, b5 = fonk1()
a4 = 32454324564335645345643
b6 = times(private_key_Alice, b5)
b7 = times(private_key_Bob, b4)
b8 = b4
b9 = add(encode(a4, 100), b6)
b10 = (b8, b9)
b11 = subtract(b10[1], b7)
b12 = decode(b11, 100)
print("Original Message:", a4)
print("Decrypted Message:", b12)