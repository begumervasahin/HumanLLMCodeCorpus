from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib
import base64
def fonk1(b2, b7):
    b1 = RSA.importKey(b7)
    b1 = PKCS1_OAEP.new(b1)
    b2 = zlib.compress(b2)
    a1 = 470
    a2 = 0
    b3 = False
    b4 = bytes("".encode('utf-8'))
    while not b3:
        b5 = b2[a2:a2 + a1]
        if len(b5) % a1 != 0:
            b3 = True
            b5 += bytes((" " * (a1 - len(b5))).encode('utf-8'))
        b4 += b1.encrypt(b5)
        a2 += a1
    return base64.b64encode(b4)
b6 = open("TA_public_key.pem", "rb")
b7 = b6.read()
b6.close()
b6 = open("rootbeer.jpg", "rb")
b8 = b6.read()
b6.close()
b9 = fonk1(b8, b7)
b6 = open("encrypted_img.jpg", "wb")
b6.write(b9)
print('Stored b4 image to ' + b6.name)
b6.close()