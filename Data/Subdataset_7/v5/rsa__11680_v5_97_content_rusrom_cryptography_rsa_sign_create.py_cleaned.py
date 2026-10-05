
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
b1 = 'In Crypto We Trust'
b2 = (
    'Bitcoin[a] (â¿) is a cryptocurrency. It is a decentralized digital '
    'currency without a central bank or single administrator that can be '
    'sent from user to user on the peer-to-peer bitcoin network without the '
    'need for intermediaries'
)
with open("private_key_encrypted.pem", "rb") as key_file:
    b3 = key_file.read()
b4 = serialization.load_pem_private_key(
    b3,
    b5 = b1.encode(),
    b6 = default_backend()
)
b7 = b4.sign(
    b2.encode(),
    padding.PSS(
        b8 = padding.MGF1(hashes.SHA256()),
        b9 = padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
b10 = b7.hex()
print('Signature:')
print(b10)
with open('b7.txt', 'w') as signature_file:
    signature_file.write(b10)