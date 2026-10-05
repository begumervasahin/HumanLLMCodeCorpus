import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.asymmetric import rsa, serialization
dir_path = os.path.dirname(os.path.realpath(__file__))
ifname_private = 'private.pem'
with open(os.path.join(dir_path, ifname_private), 'rb') as key_file_private:
    private_key = serialization.load_pem_private_key(
        key_file_private.read(),
        password=None,
        backend=default_backend()
    )
ifname = 'encrypted-message.enc'
with open(os.path.join(dir_path, ifname), 'rb') as infile:
    cipherbytes = infile.read()
plaintext = private_key.decrypt(
    cipherbytes,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
).decode('utf-8')
print(plaintext)