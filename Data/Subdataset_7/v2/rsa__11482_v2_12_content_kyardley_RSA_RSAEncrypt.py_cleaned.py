from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib
import base64
def fonk1(blob, public_key):
    b1 = RSA.import_key(public_key)
    b2 = PKCS1_OAEP.new(b1)
    b3 = zlib.compress(blob)
    a1 = 470
    a2 = 0
    b4 = bytes()
    while a2 < len(b3):
        b5 = b3[a2:a2 + a1]
        if len(b5) % a1 != 0:
            b6 = b" " * (a1 - len(b5))
            b5 += b6
        b4 += b2.encrypt(b5)
        a2 += a1
    return base64.b64encode(b4)
with open("TA_public_key.pem", "rb") as public_key_file:
    b1 = public_key_file.read()
with open("rootbeer.jpg", "rb") as image_file:
    b7 = image_file.read()
b8 = fonk1(b7, b1)
with open("encrypted_img.jpg", "wb") as encrypted_image_file:
    encrypted_image_file.write(b8)
    print('Stored encrypted image to', encrypted_image_file.name)