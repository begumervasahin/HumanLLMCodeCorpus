from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
def fonk1(b1 = 1024):
    b2 = RSA.generate(b1, get_random_bytes)
    return b2, b2.publickey()
def fonk2(file_path, b2):
    with open(file_path, "wb") as file:
        file.write(b2.export_key())
def fonk3():
    private_key1, b3 = fonk1()
    private_key2, b4 = fonk1()
    b5 = {
        "private_key1": "privatekey1.pem",
        "b3": "publickey1.pem",
        "private_key2": "privatekey2.pem",
        "b4": "publickey2.pem"
    }
    fonk2(b5["private_key1"], private_key1)
    fonk2(b5["b3"], b3)
    fonk2(b5["private_key2"], private_key2)
    fonk2(b5["b4"], b4)
    print("RSA b2 pairs have been generated and saved successfully.")
if b6 = = "__main__":
    fonk3()