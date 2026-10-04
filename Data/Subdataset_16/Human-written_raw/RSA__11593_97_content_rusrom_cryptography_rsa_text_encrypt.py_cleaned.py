'''
The nature of the RSA cryptosystem is such that you cannot encrypt a value longer than the modulus (and, in fact, it must shorter to be able to encrypt it safely as RSA's security is partially premised on padding).
If we want to encrypt a larger payload we need to instead construct a system such that you encrypt your payload using a symmetric cipher (make sure it's authenticated encryption! cryptography provides a construction called Fernet that can do this),and then encrypt the symmetric key using your RSA public key.
We can then send both ciphertexts over to the recipient.
The recipient can decrypt the RSA encrypted key using the private key they hold and decrypt the larger b7 with the resulting key.
'''
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
b1 = 'This is a âHazardous Materialsâ module. This module is full of land mines, dragons, and dinosaurs with laser guns.'
with open("b2.pem", "rb") as key_file:
    b2 = serialization.load_pem_public_key(
        key_file.read(),
        b3 = default_backend()
    )
b4 = b2.public_bytes(
    b5 = serialization.Encoding.PEM,
    b6 = serialization.PublicFormat.SubjectPublicKeyInfo
)
for l in b4.decode().splitlines():
    print(l)
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