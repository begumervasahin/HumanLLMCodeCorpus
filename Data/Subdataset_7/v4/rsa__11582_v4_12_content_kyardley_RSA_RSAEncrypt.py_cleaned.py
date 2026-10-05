import zlib
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
def fonk1(b2, b7):
    b1 = RSA.importKey(b7)
    b1 = PKCS1_OAEP.new(b1)
    b2 = zlib.compress(b2)
    a1 = 470
    a2 = 0
    b3 = False
    b4 = b''
    while not b3:
        b5 = b2[a2:a2 + a1]
        if len(b5) % a1 != 0:
            b3 = True
            b5 += b" " * (a1 - len(b5))
        b4 += b1.encrypt(b5)
        a2 += a1
    b6 = base64.b64encode(b4)
    return b6
with open("TA_public_key.pem", "rb") as fd:
    b7 = fd.read()
with open("rootbeer.jpg", "rb") as fd:
    b8 = fd.read()
b9 = fonk1(b8, b7)
with open("encrypted_img.jpg", "wb") as fd:
    fd.write(b9)
    print('Stored b4 image to', fd.name)