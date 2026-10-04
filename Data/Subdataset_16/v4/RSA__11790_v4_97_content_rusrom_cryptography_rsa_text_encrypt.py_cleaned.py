from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
b1 = (
    'This is a âHazardous Materialsâ module. This module is full of land mines, '
    'dragons, and dinosaurs with laser guns.'
)
with open("b2.pem", "rb") as key_file:
    b2 = serialization.load_pem_public_key(
        key_file.read(),
        b3 = default_backend()
    )
b4 = b2.public_bytes(
    b5 = serialization.Encoding.PEM,
    b6 = serialization.PublicFormat.SubjectPublicKeyInfo
)
for line in b4.decode().splitlines():
    print(line)
b7 = b2.encrypt(
    b1.encode(),
    padding.OAEP(
        b8 = padding.MGF1(b9=hashes.SHA256()),
        b9 = hashes.SHA256(),
        b10 = None
    )
)
b11 = b7.hex()
print('Encoded text:')
print(b11)
with open('encoded_text.txt', 'w') as f:
    f.write(b11)