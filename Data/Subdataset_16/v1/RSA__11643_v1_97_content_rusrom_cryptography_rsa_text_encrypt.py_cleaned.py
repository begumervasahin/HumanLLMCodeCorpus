from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import keywrap
from cryptography.b13 import Fernet
import base64
import os
def fonk1():
    b1 = rsa.generate_private_key(
        b2 = 65537,
        b3 = 2048,
        b4 = default_backend()
    )
    b5 = b1.b5()
    with open("b1.pem", "wb") as private_key_file:
        private_key_file.write(
            b1.private_bytes(
                b6 = serialization.Encoding.PEM,
                b7 = serialization.PrivateFormat.TraditionalOpenSSL,
                b8 = serialization.NoEncryption()
            )
        )
    with open("b5.pem", "wb") as public_key_file:
        public_key_file.write(
            b5.public_bytes(
                b6 = serialization.Encoding.PEM,
                b7 = serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )
def fonk2(path):
    with open(path, "rb") as key_file:
        b5 = serialization.load_pem_public_key(
            key_file.read(),
            b4 = default_backend()
        )
    return b5
def fonk3(b15, b5):
    b9 = b5.encrypt(
        b15,
        padding.OAEP(
            b10 = padding.MGF1(b11=hashes.SHA256()),
            b11 = hashes.SHA256(),
            b12 = None
        )
    )
    return b9
def fonk4(payload, b15):
    b13 = Fernet(b15)
    b14 = b13.encrypt(payload.encode())
    return b14
if not os.path.exists("b5.pem") or not os.path.exists("b1.pem"):
    fonk1()
b5 = fonk2("b5.pem")
b15 = Fernet.generate_key()
b16 = 'This is a âHazardous Materialsâ module. This module is full of land mines, dragons, and dinosaurs with laser guns.'
b14 = fonk4(b16, b15)
b9 = fonk3(b15, b5)
with open('b9.bin', 'wb') as f:
    f.write(b9)
with open('b14.bin', 'wb') as f:
    f.write(b14)
print("Encryption complete. Encrypted symmetric key and payload have been saved to files.")