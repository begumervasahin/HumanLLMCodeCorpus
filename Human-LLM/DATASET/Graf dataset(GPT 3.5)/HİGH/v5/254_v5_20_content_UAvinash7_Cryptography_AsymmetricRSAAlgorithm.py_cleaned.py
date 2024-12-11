from Crypto.PublicKey import RSA
from Crypto import Random
import ast
def fonk1():
    b1 = Random.new().read
    b2 = RSA.generate(1024, b1)
    return b2
def fonk2(b5, message):
    b3 = b5.encrypt(message.encode(), 32)
    return b3
def fonk3(b2, b3):
    b4 = b2.decrypt(ast.literal_eval(str(b3)))
    return b4.decode()
def fonk4():
    b2 = fonk1()
    b5 = b2.publickey()
    b6 = "Hello World"
    b3 = fonk2(b5, b6)
    print("Encrypted Text:", b3)
    b4 = fonk3(b2, b3)
    print("Decrypted Text:", b4)
if b7 = = "__main__":
    fonk4()