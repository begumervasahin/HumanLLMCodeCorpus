from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.b14 import Fernet
import os
def fonk1(b1 = "b2.pem", b16="b6.pem"):
    b2 = rsa.generate_private_key(
        b3 = 65537,
        b4 = 2048,
        b5 = default_backend()
    )
    b6 = b2.b6()
    with open(b1, "wb") as private_key_file:
        private_key_file.write(
            b2.private_bytes(
                b7 = serialization.Encoding.PEM,
                b8 = serialization.PrivateFormat.TraditionalOpenSSL,
                b9 = serialization.NoEncryption()
            )
        )
    with open(b16, "wb") as public_key_file:
        public_key_file.write(
            b6.public_bytes(
                b7 = serialization.Encoding.PEM,
                b8 = serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )
def fonk2(path):
    with open(path, "rb") as key_file:
        b6 = serialization.load_pem_public_key(
            key_file.read(),
            b5 = default_backend()
        )
    return b6
def fonk3(b17, b6):
    b10 = b6.encrypt(
        b17,
        padding.OAEP(
            b11 = padding.MGF1(b12=hashes.SHA256()),
            b12 = hashes.SHA256(),
            b13 = None
        )
    )
    return b10
def fonk4(payload, b17):
    b14 = Fernet(b17)
    b15 = b14.encrypt(payload.encode())
    return b15
def fonk5():
    b1 = "b2.pem"
    b16 = "b6.pem"
    if not os.path.exists(b16) or not os.path.exists(b1):
        fonk1(b1, b16)
    b6 = fonk2(b16)
    b17 = Fernet.generate_key()
    b18 = 'This is a âHazardous Materialsâ module. This module is full of land mines, dragons, and dinosaurs with laser guns.'
    b15 = fonk4(b18, b17)
    b10 = fonk3(b17, b6)
    with open('b10.bin', 'wb') as f:
        f.write(b10)
    with open('b15.bin', 'wb') as f:
        f.write(b15)
    print("Encryption complete. Encrypted symmetric key and payload have been saved to files.")
if b19 = = "__main__":
    fonk5()