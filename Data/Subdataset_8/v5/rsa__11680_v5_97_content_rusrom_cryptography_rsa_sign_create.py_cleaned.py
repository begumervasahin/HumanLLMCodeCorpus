
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
PASSWORD = 'In Crypto We Trust'
MESSAGE = (
    'Bitcoin[a] (â¿) is a cryptocurrency. It is a decentralized digital '
    'currency without a central bank or single administrator that can be '
    'sent from user to user on the peer-to-peer bitcoin network without the '
    'need for intermediaries'
)
with open("private_key_encrypted.pem", "rb") as key_file:
    encrypted_private_key = key_file.read()
private_key = serialization.load_pem_private_key(
    encrypted_private_key,
    password=PASSWORD.encode(),
    backend=default_backend()
)
signature = private_key.sign(
    MESSAGE.encode(),
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
signature_hex = signature.hex()
print('Signature:')
print(signature_hex)
with open('signature.txt', 'w') as signature_file:
    signature_file.write(signature_hex)