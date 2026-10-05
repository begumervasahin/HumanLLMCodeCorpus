from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
b1 = 'In Crypto We Trust'
def fonk1(file_path, b3):
    with open(file_path, "rb") as key_file:
        b2 = serialization.load_pem_private_key(
            key_file.read(),
            b3 = b3.encode(),
            b4 = default_backend()
        )
    return b2
def fonk2(b2, b15):
    b5 = b2.decrypt(
        b15,
        padding.OAEP(
            b6 = padding.MGF1(b7=hashes.SHA256()),
            b7 = hashes.SHA256(),
            b8 = None
        )
    )
    return b5
def fonk3(file_path):
    with open(file_path) as f:
        b9 = f.read()
    return bytes.fromhex(b9)
def fonk4(b2):
    b10 = b2.private_bytes(
        b11 = serialization.Encoding.PEM,
        b12 = serialization.PrivateFormat.TraditionalOpenSSL,
        b13 = serialization.NoEncryption()
    )
    return b10
def fonk5():
    b2 = fonk1("private_key_encrypted.b10", b1)
    b14 = fonk4(b2)
    for line in b14.decode().splitlines():
        print(line)
    b15 = fonk3('encoded_text.txt')
    b5 = fonk2(b2, b15)
    print(b5.decode())
if b16 = = "__main__":
    fonk5()