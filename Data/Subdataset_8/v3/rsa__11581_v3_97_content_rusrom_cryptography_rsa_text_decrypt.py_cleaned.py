from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
PASSWORD = 'In Crypto We Trust'
def load_private_key(file_path, password):
    with open(file_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=password.encode(),
            backend=default_backend()
        )
    return private_key
def decrypt_text(private_key, ciphertext):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext
def read_ciphertext(file_path):
    with open(file_path) as f:
        ciphertext_string = f.read()
    return bytes.fromhex(ciphertext_string)
def convert_to_pem(private_key):
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    return pem
def main():
    private_key = load_private_key("private_key_encrypted.pem", PASSWORD)
    pem_private_key = convert_to_pem(private_key)
    for line in pem_private_key.decode().splitlines():
        print(line)
    ciphertext = read_ciphertext('encoded_text.txt')
    plaintext = decrypt_text(private_key, ciphertext)
    print(plaintext.decode())
if __name__ == "__main__":
    main()