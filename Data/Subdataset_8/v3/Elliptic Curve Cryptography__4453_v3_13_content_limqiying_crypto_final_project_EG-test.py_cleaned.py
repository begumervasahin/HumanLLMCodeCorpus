
from ecc_simple import set_p256_param, times, add, subtract, encode, decode
import random
def generate_key_pair():
    private_key = random.randrange(1, p)
    public_key = times(private_key, g)
    return private_key, public_key
set_p256_param()
p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
x = 48439561293906451759052585252797914202762949526041747995844080717082404635286
y = 36134250956749795798585127919587881956611106672985015071877198253568414405109
g = (x, y)
private_key_Alice, public_key_Alice = generate_key_pair()
private_key_Bob, public_key_Bob = generate_key_pair()
message = 32454324564335645345643
shared_key_Alice = times(private_key_Alice, public_key_Bob)
shared_key_Bob = times(private_key_Bob, public_key_Alice)
c_1 = public_key_Alice
c_2 = add(encode(message, 100), shared_key_Alice)
ciphertext = (c_1, c_2)
plaintext = subtract(ciphertext[1], shared_key_Bob)
decoded_message = decode(plaintext, 100)
print("Original Message:", message)
print("Decrypted Message:", decoded_message)