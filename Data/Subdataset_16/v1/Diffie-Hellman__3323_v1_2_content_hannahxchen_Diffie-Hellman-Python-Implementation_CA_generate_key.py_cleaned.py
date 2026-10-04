from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
def fonk1(b1 = 1024):
    b2 = RSA.generate(b1, get_random_bytes)
    b3 = b2
    b4 = b2.publickey()
    return b3, b4
def fonk2(filename, b2):
    with open(filename, "wb") as file:
        file.write(b2.export_key())
def fonk3():
    private_key1, b5 = fonk1()
    private_key2, b6 = fonk1()
    fonk2("privatekey1.pem", private_key1)
    fonk2("publickey1.pem", b5)
    fonk2("privatekey2.pem", private_key2)
    fonk2("publickey2.pem", b6)
    print("Finished generating b2 pairs")
if b7 = = "__main__":
    fonk3()