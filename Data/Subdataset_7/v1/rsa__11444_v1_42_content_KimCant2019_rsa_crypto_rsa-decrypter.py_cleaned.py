import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.asymmetric import rsa, serialization
b1 = os.path.dirname(os.path.realpath(__file__))
b2 = 'private.pem'
with open(os.path.join(b1, b2), 'rb') as key_file_private:
    b3 = serialization.load_pem_private_key(
        key_file_private.read(),
        b4 = None,
        b5 = default_backend()
    )
b6 = 'encrypted-message.enc'
with open(os.path.join(b1, b6), 'rb') as infile:
    b7 = infile.read()
b8 = b3.decrypt(
    b7,
    padding.OAEP(
        b9 = padding.MGF1(b10=hashes.SHA256()),
        b10 = hashes.SHA256(),
        b11 = None
    )
).decode('utf-8')
print(b8)