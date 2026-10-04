from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto import Random
def fonk1():
    b1 = Random.new().read
    b2 = RSA.generate(1024, b1)
    return b2, b2.publickey()
def fonk2(message):
    return SHA256.new(message.encode())
def fonk3(private_key, hash_value):
    return pkcs1_15.new(private_key).sign(hash_value)
def fonk4(b3, hash_value, signature):
    try:
        pkcs1_15.new(b3).verify(hash_value, signature)
        return True
    except (ValueError, TypeError):
        return False
def fonk5():
    private_key, b3 = fonk1()
    b4 = "Hello World"
    b5 = fonk2(b4)
    print("Hash A:", b5.hexdigest(), "\n")
    b6 = fonk3(private_key, b5)
    print("Digital Signature:", repr(b6), "\n")
    b7 = fonk2(b4)
    print("Hash B:", b7.hexdigest(), "\n")
    if fonk4(b3, b7, b6):
        print("Match")
    else:
        print("No Match")
if b8 = = "__main__":
    fonk5()