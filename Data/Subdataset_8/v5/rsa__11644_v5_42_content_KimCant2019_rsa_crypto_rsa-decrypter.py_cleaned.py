import os
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
dir_path = os.path.dirname(os.path.realpath(__file__))
private_key_filename = 'private.pem'
encrypted_message_filename = 'encrypted-message.enc'
with open(os.path.join(dir_path, private_key_filename), 'rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )
with open(os.path.join(dir_path, encrypted_message_filename), 'rb') as encrypted_file:
    encrypted_message = encrypted_file.read()
plaintext = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
).decode('utf-8')
print(plaintext)