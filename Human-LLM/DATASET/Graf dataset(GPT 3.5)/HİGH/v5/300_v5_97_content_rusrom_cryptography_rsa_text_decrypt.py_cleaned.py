from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
def fonk1(b14, b3):
    with open(b14, "rb") as key_file:
        b1 = key_file.read()
        b2 = serialization.load_pem_private_key(
            b1,
            b3 = b3.encode(),
            b4 = default_backend()
        )
    return b2
def fonk2(b2):
    b5 = b2.private_bytes(
        b6 = serialization.Encoding.PEM,
        b7 = serialization.PrivateFormat.TraditionalOpenSSL,
        b8 = serialization.NoEncryption()
    )
    return b5.decode()
def fonk3(b2, b15):
    with open(b15, 'r') as f:
        b9 = bytes.fromhex(f.read())
    b10 = b2.decrypt(
        b9,
        padding.OAEP(
            b11 = padding.MGF1(b12=hashes.SHA256()),
            b12 = hashes.SHA256(),
            b13 = None
        )
    )
    return b10.decode()
def fonk4():
    b14 = "private_key_encrypted.pem"
    b15 = "encoded_text.txt"
    b3 = 'In Crypto We Trust'
    b2 = fonk1(b14, b3)
    b5 = fonk2(b2)
    b16 = fonk3(b2, b15)
    print("Decrypted Private Key:")
    print(b5)
    print("\nDecrypted Text:")
    print(b16)
if b17 = = "__main__":
    fonk4()