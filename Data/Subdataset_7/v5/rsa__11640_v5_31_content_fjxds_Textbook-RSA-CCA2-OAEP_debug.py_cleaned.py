import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random
def fonk1(key_path):
    with open(key_path, "rb") as key_file:
        b1 = key_file.read()
        b2 = RSA.importKey(b1)
    return b2
def fonk2(b7, b2):
    b3 = PKCS1_v1_5.new(b2)
    b4 = b3.decrypt(b7, Random.new().read)
    return b4.decode()
def fonk3():
    b5 = "secret.txt"
    b6 = "rsa_private_key.pem"
    with open(b5, "rb") as file:
        b7 = base64.b64decode(file.read())
    b2 = fonk1(b6)
    b4 = fonk2(b7, b2)
    print("Decrypted data:", b4)
if b8 = = "__main__":
    fonk3()