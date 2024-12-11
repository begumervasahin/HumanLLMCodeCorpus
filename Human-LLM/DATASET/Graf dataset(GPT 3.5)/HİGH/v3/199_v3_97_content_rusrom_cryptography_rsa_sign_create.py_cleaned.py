
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
b1 = 'In Crypto We Trust'
b2 = 'Bitcoin[a] (â¿) is a cryptocurrency. It is a decentralized digital currency without a central bank or single administrator that can be sent from user to user on the peer-to-peer bitcoin network without the need for intermediaries'
b3 = "private_key_encrypted.pem"
b4 = "b8.txt"
with open(b3, "rb") as key_file:
    b5 = serialization.load_pem_private_key(
        key_file.read(),
        b6 = b1.encode(),
        b7 = default_backend()
    )
b8 = b5.sign(
    b2.encode(),
    padding.PSS(
        b9 = padding.MGF1(hashes.SHA256()),
        b10 = padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
b11 = b8.hex()
with open(b4, 'w') as signature_file:
    signature_file.write(b11)
print('Signature:')
print(b11)