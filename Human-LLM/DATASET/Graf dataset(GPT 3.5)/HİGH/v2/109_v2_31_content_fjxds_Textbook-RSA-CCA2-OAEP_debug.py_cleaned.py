import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random
import rsa
b1 = "secret.txt"
with open(b1, "rb") as file:
    b2 = file.read()
b3 = base64.b64decode(b2)
b4 = "rsa_private_key.pem"
with open(b4, "rb") as key_file:
    b5 = key_file.read()
    b6 = RSA.importKey(b5)
b7 = PKCS1_v1_5.new(b6)
b8 = b7.decrypt(b3, Random.new().read)
print("Decrypted using Crypto module PKCS1_v1_5:", b8)
b9 = rsa.PrivateKey.load_pkcs1(b5)
b10 = rsa.decrypt(b3, b9)
print("Decrypted using rsa module:", b10)