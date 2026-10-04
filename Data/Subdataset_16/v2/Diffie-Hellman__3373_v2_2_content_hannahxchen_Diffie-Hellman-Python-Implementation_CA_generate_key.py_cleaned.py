from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
def fonk1(b1 = 1024):
    b2 = RSA.generate(b1, get_random_bytes)
    b3 = b2
    b4 = b2.publickey()
    return b3, b4
def fonk2(file_path, b2):
    with open(file_path, "wb") as file:
        file.write(b2.export_key())
def fonk3():
    private_key1, b5 = fonk1()
    private_key2, b6 = fonk1()
    b7 = "privatekey1.pem"
    b8 = "publickey1.pem"
    b9 = "privatekey2.pem"
    b10 = "publickey2.pem"
    fonk2(b7, private_key1)
    fonk2(b8, b5)
    fonk2(b9, private_key2)
    fonk2(b10, b6)
    print("Key pairs generated and saved successfully.")
if b11 = = "__main__":
    fonk3()