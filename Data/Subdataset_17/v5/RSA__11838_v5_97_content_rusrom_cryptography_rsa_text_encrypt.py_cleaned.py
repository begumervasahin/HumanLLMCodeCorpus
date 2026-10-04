from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
TEXT_TO_ENCRYPT = (
    'This is a âHazardous Materialsâ module. This module is full of land mines, '
    'dragons, and dinosaurs with laser guns.'
)
def load_public_key(pem_file_path):
    with open(pem_file_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return public_key
def serialize_public_key_to_pem(public_key):
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return public_pem.decode()
def encrypt_text(public_key, text):
    ciphertext = public_key.encrypt(
        text.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext
def save_ciphertext_to_file(ciphertext, file_path):
    with open(file_path, 'w') as f:
        f.write(ciphertext.hex())
public_key = load_public_key("public_key.pem")
public_pem = serialize_public_key_to_pem(public_key)
print("Public Key in PEM Format:")
print(public_pem)
ciphertext = encrypt_text(public_key, TEXT_TO_ENCRYPT)
ciphertext_string = ciphertext.hex()
print('Encoded text:')
print(ciphertext_string)
save_ciphertext_to_file(ciphertext, 'encoded_text.txt')