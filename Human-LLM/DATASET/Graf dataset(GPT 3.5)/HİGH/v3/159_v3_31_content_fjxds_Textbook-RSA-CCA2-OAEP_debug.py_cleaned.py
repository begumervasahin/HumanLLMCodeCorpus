import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random
import rsa
def fonk1(file_path):
    with open(file_path, "rb") as file:
        return file.read()
def fonk2(data):
    return base64.b64decode(data)
def fonk3(private_key_path):
    with open(private_key_path, "rb") as key_file:
        b1 = key_file.read()
        return RSA.importKey(b1)
def fonk4(b4, b5):
    b2 = PKCS1_v1_5.new(b5)
    return b2.decrypt(b4, Random.new().read)
def fonk5(b4, b7):
    return rsa.decrypt(b4, b7)
def fonk6():
    b3 = fonk1("secret.txt")
    b4 = fonk2(b3)
    b5 = fonk3("rsa_private_key.pem")
    b6 = fonk4(b4, b5)
    print("Decrypted using Crypto module PKCS1_v1_5:", b6)
    b7 = rsa.PrivateKey.load_pkcs1(b5.export_key())
    b8 = fonk5(b4, b7)
    print("Decrypted using rsa module:", b8)
if b9 = = "__main__":
    fonk6()