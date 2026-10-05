
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
PASSWORD = 'In Crypto We Trust'
MESSAGE = 'Bitcoin[a] (â¿) is a cryptocurrency. It is a decentralized digital currency without a central bank or single administrator that can be sent from user to user on the peer-to-peer bitcoin network without the need for intermediaries'
PRIVATE_KEY_FILE = "private_key_encrypted.pem"
SIGNATURE_FILE = "signature.txt"
with open(PRIVATE_KEY_FILE, "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
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
with open(SIGNATURE_FILE, 'w') as signature_file:
    signature_file.write(signature_hex)
print('Signature:')
print(signature_hex)