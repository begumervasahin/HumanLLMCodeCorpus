
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
b1 = 'In Crypto We Trust'
b2 = 'Bitcoin[a] (â¿) is a cryptocurrency. It is a decentralized digital currency without a central bank or single administrator that can be sent from user to user on the peer-to-peer bitcoin network without the need for intermediaries'
with open("private_key_encrypted.pem", "rb") as key_file:
    b3 = serialization.load_pem_private_key(
        key_file.read(),
        b4 = b1.encode(),
        b5 = default_backend()
    )
b6 = b3.sign(
    b2.encode(),
    padding.PSS(
        b7 = padding.MGF1(hashes.SHA256()),
        b8 = padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
b9 = b6.hex()
print('Signature:')
print(b9)
with open('b6.txt', 'w') as f:
    f.write(b9)