import os
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
b1 = os.path.dirname(os.path.realpath(__file__))
b2 = 'private.pem'
b3 = 'encrypted-message.enc'
with open(os.path.join(b1, b2), 'rb') as key_file:
    b4 = serialization.load_pem_private_key(
        key_file.read(),
        b5 = None,
        b6 = default_backend()
    )
with open(os.path.join(b1, b3), 'rb') as encrypted_file:
    b7 = encrypted_file.read()
b8 = b4.decrypt(
    b7,
    padding.OAEP(
        b9 = padding.MGF1(b10=hashes.SHA256()),
        b10 = hashes.SHA256(),
        b11 = None
    )
).decode('utf-8')
print(b8)