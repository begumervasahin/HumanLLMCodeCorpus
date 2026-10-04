from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import keywrap
from cryptography.fernet import Fernet
import base64
import os
def generate_rsa_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    with open("private_key.pem", "wb") as private_key_file:
        private_key_file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
        )
    with open("public_key.pem", "wb") as public_key_file:
        public_key_file.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )
def load_public_key(path):
    with open(path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return public_key
def encrypt_symmetric_key_with_rsa(symmetric_key, public_key):
    encrypted_symmetric_key = public_key.encrypt(
        symmetric_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_symmetric_key
def encrypt_payload_with_fernet(payload, symmetric_key):
    fernet = Fernet(symmetric_key)
    encrypted_payload = fernet.encrypt(payload.encode())
    return encrypted_payload
if not os.path.exists("public_key.pem") or not os.path.exists("private_key.pem"):
    generate_rsa_key_pair()
public_key = load_public_key("public_key.pem")
symmetric_key = Fernet.generate_key()
TEXT_TO_ENCRYPT = 'This is a âHazardous Materialsâ module. This module is full of land mines, dragons, and dinosaurs with laser guns.'
encrypted_payload = encrypt_payload_with_fernet(TEXT_TO_ENCRYPT, symmetric_key)
encrypted_symmetric_key = encrypt_symmetric_key_with_rsa(symmetric_key, public_key)
with open('encrypted_symmetric_key.bin', 'wb') as f:
    f.write(encrypted_symmetric_key)
with open('encrypted_payload.bin', 'wb') as f:
    f.write(encrypted_payload)
print("Encryption complete. Encrypted symmetric key and payload have been saved to files.")