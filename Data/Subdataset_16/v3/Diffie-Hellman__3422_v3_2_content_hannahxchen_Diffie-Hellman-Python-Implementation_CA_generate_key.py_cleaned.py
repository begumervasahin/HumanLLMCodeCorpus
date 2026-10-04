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
        "privatekey1": "privatekey1.pem",
        "publickey1": "publickey1.pem",
        "privatekey2": "privatekey2.pem",
        "publickey2": "publickey2.pem"
    }
    fonk2(b5["privatekey1"], private_key1)
    fonk2(b5["publickey1"], b3)
    fonk2(b5["privatekey2"], private_key2)
    fonk2(b5["publickey2"], b4)
    print("Key pairs generated and saved successfully.")
if b6 = = "__main__":
    fonk3()