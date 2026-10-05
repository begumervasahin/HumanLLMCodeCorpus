
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
PASSWORD = 'In Crypto We Trust'
with open("private_key_encrypted.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=PASSWORD.encode(),
        backend=default_backend()
    )
pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)
for line in pem.decode().splitlines():
    print(line)
with open('encoded_text.txt') as f:
    ciphertext_string = f.read()
ciphertext = bytes.fromhex(ciphertext_string)
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(plaintext.decode())
