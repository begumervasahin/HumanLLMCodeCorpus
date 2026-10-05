from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
b1 = 'In Crypto We Trust'
with open("private_key_encrypted.b5", "rb") as key_file:
    b2 = serialization.load_pem_private_key(
        key_file.read(),
        b3 = b1.encode(),
        b4 = default_backend()
    )
b5 = b2.private_bytes(
    b6 = serialization.Encoding.PEM,
    b7 = serialization.PrivateFormat.TraditionalOpenSSL,
    b8 = serialization.NoEncryption()
)
for line in b5.decode().splitlines():
    print(line)
with open('encoded_text.txt') as f:
    b9 = f.read()
b10 = bytes.fromhex(b9)
b11 = b2.decrypt(
    b10,
    padding.OAEP(
        b12 = padding.MGF1(b13=hashes.SHA256()),
        b13 = hashes.SHA256(),
        b14 = None
    )
)
print(b11.decode())