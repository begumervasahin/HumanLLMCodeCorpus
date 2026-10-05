import base64
import cryptography
import binascii
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
dir_path = os.path.dirname(os.path.realpath(__file__))
ifname_private = 'private.pem'
with open(dir_path + '/' + ifname_private, 'r') as key_file_private :
    private_key = serialization.load_pem_private_key(
        key_file_private.read().encode('utf-8'),
        password=None,
        backend=default_backend()
    )
ifname = 'encrypted-message.enc'
cipherbytes = bytearray()
with open(dir_path + '/' + ifname,'rb') as infile:
    cipherbytes = infile.read()
plaintext = private_key.decrypt(cipherbytes,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None )).decode('utf-8')
print( plaintext )