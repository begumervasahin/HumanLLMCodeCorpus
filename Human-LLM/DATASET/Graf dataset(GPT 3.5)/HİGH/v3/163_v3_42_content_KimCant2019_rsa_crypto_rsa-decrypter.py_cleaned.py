import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.asymmetric import rsa, serialization
def fonk1(key_file_path):
    with open(key_file_path, 'rb') as key_file:
        return serialization.load_pem_private_key(
            key_file.read(),
            b1 = None,
            b2 = default_backend()
        )
def fonk2(message_file_path):
    with open(message_file_path, 'rb') as message_file:
        return message_file.read()
def fonk3(b8, b10):
    return b8.decrypt(
        b10,
        padding.OAEP(
            b3 = padding.MGF1(b4=hashes.SHA256()),
            b4 = hashes.SHA256(),
            b5 = None
        )
    ).decode('utf-8')
def fonk4():
    b6 = os.path.dirname(os.path.realpath(__file__))
    b7 = os.path.join(b6, 'private.pem')
    b8 = fonk1(b7)
    b9 = os.path.join(b6, 'encrypted-message.enc')
    b10 = fonk2(b9)
    b11 = fonk3(b8, b10)
    print("Decrypted message:\n", b11)
if b12 = = "__main__":
    fonk4()