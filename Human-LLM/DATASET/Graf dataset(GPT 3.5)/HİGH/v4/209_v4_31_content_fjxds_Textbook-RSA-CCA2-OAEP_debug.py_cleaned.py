import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random
b1 = Random.new().read
b2 = "secret.txt"
with open(b2, "rb") as f:
    b3 = f.read()
    b4 = base64.b64decode(b3)
    print(b4)
b5 = "rsa_private_key.pem"
a1 = 117
with open(b5, "rb") as f:
    b6 = f.read()
    b7 = RSA.importKey(b6)
    b8 = PKCS1_v1_5.new(b7)
    b9 = b8.decrypt(b4, b1)
    print(b9.decode())
