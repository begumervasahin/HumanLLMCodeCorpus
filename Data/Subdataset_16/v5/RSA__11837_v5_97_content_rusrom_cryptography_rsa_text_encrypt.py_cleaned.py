from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
b1 = (
    'This is a âHazardous Materialsâ module. This module is full of land mines, '
    'dragons, and dinosaurs with laser guns.'
)
def fonk1(pem_file_path):
    with open(pem_file_path, "rb") as key_file:
        b2 = serialization.load_pem_public_key(
            key_file.read(),
            b3 = default_backend()
        )
    return b2
def fonk2(b2):
    b4 = b2.public_bytes(
        b5 = serialization.Encoding.PEM,
        b6 = serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return b4.decode()
def fonk3(b2, text):
    b7 = b2.encrypt(
        text.encode(),
        padding.OAEP(
            b8 = padding.MGF1(b9=hashes.SHA256()),
            b9 = hashes.SHA256(),
            b10 = None
        )
    )
    return b7
def fonk4(b7, file_path):
    with open(file_path, 'w') as f:
        f.write(b7.hex())
b2 = fonk1("b2.pem")
b4 = fonk2(b2)
print("Public Key in PEM Format:")
print(b4)
b7 = fonk3(b2, b1)
b11 = b7.hex()
print('Encoded text:')
print(b11)
fonk4(b7, 'encoded_text.txt')