from ecc_simple import *
import random
set_p256_param()
p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
x = 48439561293906451759052585252797914202762949526041747995844080717082404635286
y = 36134250956749795798585127919587881956611106672985015071877198253568414405109
g = (x, y)
a = random.randrange(1, p)
b = random.randrange(1, p)
public_Bob = times(b, g)
public_Alice = times(a, g)
m = 32454324564335645345643
shared_key_A = times(a, public_Bob)
shared_key_B = times(b, public_Alice)
c_1 = public_Alice
c_2 = add(encode(m, 100), shared_key_A)
ciphertext = (c_1, c_2)
plaintext = subtract(ciphertext[1], shared_key_B)
decoded_message = decode(plaintext, 100)
print("Original Message:", m)
print("Decrypted Message:", decoded_message)