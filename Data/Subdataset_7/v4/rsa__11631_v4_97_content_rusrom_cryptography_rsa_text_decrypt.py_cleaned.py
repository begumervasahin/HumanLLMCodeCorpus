from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
b1 = 'In Crypto We Trust'
with open("private_key_encrypted.pem", "rb") as key_file:
    b2 = key_file.read()
    b3 = serialization.load_pem_private_key(
        b2,
        b4 = b1.encode(),
        b5 = default_backend()
    )
b6 = b3.private_bytes(
    b7 = serialization.Encoding.PEM,
    b8 = serialization.PrivateFormat.TraditionalOpenSSL,
    b9 = serialization.NoEncryption()
)
for line in b6.decode().splitlines():
    print(line)
with open('encoded_text.txt') as f:
    b10 = f.read()
b11 = bytes.fromhex(b10)
b12 = b3.decrypt(
    b11,
    padding.OAEP(
        b13 = padding.MGF1(b14=hashes.SHA256()),
        b14 = hashes.SHA256(),
        b15 = None
    )
)
print(b12.decode())
