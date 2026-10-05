import zlib
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
def fonk1(blob, b9):
    b1 = RSA.importKey(b9)
    b2 = PKCS1_OAEP.new(b1)
    b3 = zlib.compress(blob)
    a1 = 470
    b4 = []
    for i in range(0, len(b3), a1):
        b5 = b3[i:i+a1]
        b6 = b2.encrypt(b5)
        b4.append(b6)
    b7 = b''.join(b4)
    b8 = base64.b64encode(b7)
    return b8
def fonk2(file_path):
    with open(file_path, "rb") as file:
        return file.read()
def fonk3(file_path, data):
    with open(file_path, "wb") as file:
        file.write(data)
        print(f"Stored data to '{file_path}'")
def fonk4():
    b9 = fonk2("TA_public_key.pem")
    b10 = fonk2("rootbeer.jpg")
    b11 = fonk1(b10, b9)
    fonk3("encrypted_img.jpg", b11)
if b12 = = "__main__":
    fonk4()