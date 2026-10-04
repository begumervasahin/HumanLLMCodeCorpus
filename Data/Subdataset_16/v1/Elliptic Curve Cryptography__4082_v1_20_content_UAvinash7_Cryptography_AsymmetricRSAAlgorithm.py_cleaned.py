from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
def fonk1():
    b1 = Random.new().read
    b2 = RSA.generate(1024, b1)
    return b2, b2.publickey()
def fonk2(b6, message):
    b3 = PKCS1_OAEP.new(b6)
    b4 = b3.encrypt(message.encode())
    return b4
def fonk3(private_key, b4):
    b3 = PKCS1_OAEP.new(private_key)
    b5 = b3.decrypt(b4)
    return b5.decode()
def fonk4():
    private_key, b6 = fonk1()
    b7 = "Hello World"
    b8 = fonk2(b6, b7)
    print("Encrypted Text:", b8)
    b9 = fonk3(private_key, b8)
    print("Decrypted Text:", b9)
if b10 = = "__main__":
    fonk4()