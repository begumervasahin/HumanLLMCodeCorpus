from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
def fonk1(b1 = 1024):
    b2 = Random.new().read
    b3 = RSA.generate(b1, b2)
    return b3
def fonk2(message):
    b4 = SHA256.new(message.encode())
    return b4.digest()
def fonk3(private_key, message_hash):
    b5 = private_key.sign(message_hash, "")
    return b5
def fonk4(b7, message_hash, b5):
    b6 = b7.verify(message_hash, b5)
    return b6
def fonk5():
    b3 = fonk1()
    b7 = b3.publickey()
    b8 = "Hello World"
    b9 = fonk2(b8)
    b5 = fonk3(b3, b9)
    print("Hash A:", repr(b9))
    print("Digital Signature:", repr(b5))
    b10 = fonk2(b8)
    print("Hash B:", repr(b10))
    b11 = fonk4(b7, b10, b5)
    if b11:
        print("Match")
    else:
        print("No Match")
if b12 = = "__main__":
    fonk5()