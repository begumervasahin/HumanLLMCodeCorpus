import zlib
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
def encrypt_blob(blob, public_key):
    rsa_key = RSA.importKey(public_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    compressed_blob = zlib.compress(blob)
    chunk_size = 470
    encrypted_chunks = []
    for i in range(0, len(compressed_blob), chunk_size):
        chunk = compressed_blob[i:i+chunk_size]
        encrypted_chunk = cipher_rsa.encrypt(chunk)
        encrypted_chunks.append(encrypted_chunk)
    encrypted_data = b''.join(encrypted_chunks)
    encoded_encrypted = base64.b64encode(encrypted_data)
    return encoded_encrypted
def read_file(file_path):
    with open(file_path, "rb") as file:
        return file.read()
def write_file(file_path, data):
    with open(file_path, "wb") as file:
        file.write(data)
        print(f"Stored data to '{file_path}'")
def main():
    public_key = read_file("TA_public_key.pem")
    unencrypted_blob = read_file("rootbeer.jpg")
    encrypted_blob = encrypt_blob(unencrypted_blob, public_key)
    write_file("encrypted_img.jpg", encrypted_blob)
if __name__ == "__main__":
    main()