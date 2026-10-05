from Crypto.PublicKey import RSA
from Crypto import Random
import ast
def fonk1():
    b1 = Random.new().read
    return RSA.generate(1024, b1)
def fonk2(b3, message):
    return b3.encrypt(message.encode(), 32)
def fonk3(b2, b5):
    return b2.decrypt(ast.literal_eval(str(b5))).decode()
def fonk4():
    b2 = fonk1()
    b3 = b2.publickey()
    b4 = "Hello World"
    b5 = fonk2(b3, b4)
    print("Encrypted Text:", b5)
    b6 = fonk3(b2, b5)
    print("Decrypted Text:", b6)
if b7 = = "__main__":
    fonk4()