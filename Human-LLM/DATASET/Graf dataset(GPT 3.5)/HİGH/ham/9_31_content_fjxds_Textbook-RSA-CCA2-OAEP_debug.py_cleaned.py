import base64
import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random
import rsa
b1 = Random.new().read
b2 = "secret.txt"
b3 = ""
with open(b2,"rb") as f:
    b4 = f.read()
    b5 = base64.b64decode(b4)
    print(b5)
b2 = "rsa_private_key.pem"
a1 = 117
with open(b2,"rb") as f:
    b6 = f.read()
    b7 = RSA.importKey(b6)
    b8 = PKCS1_v1_5.new(b7)
    b9 = rsa.PrivateKey.load_pkcs1(b6)
    '''b10 = len(encrypted_byte)
    if b10 < a1:
        b11 = b8.decrypt(encrypted_byte, 'failure')
    else:
        a2 = 0
        b12 = []
        while b10 - a2 > 0:
            if b10 - a2 > a1:
                b12.append(b8.decrypt(encrypted_byte[a2: a2 + a1], 'failure'))
            else:
                b12.append(b8.decrypt(encrypted_byte[a2:], 'failure'))
            a2 += a1
        b11 = b''.join(b12)
    b13 = b11.decode()'''
    print(b8.decrypt(b5,b1))
    rsa.decrypt(b5, b9)