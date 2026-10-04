from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
TEXT_TO_ENCRYPT = (
    'This is a âHazardous Materialsâ module. This module is full of land mines, '
    'dragons, and dinosaurs with laser guns.'
)
with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
for line in public_pem.decode().splitlines():
    print(line)
ciphertext = public_key.encrypt(
    TEXT_TO_ENCRYPT.encode(),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
ciphertext_string = ciphertext.hex()
print('Encoded text:')
print(ciphertext_string)
with open('encoded_text.txt', 'w') as f:
    f.write(ciphertext_string)