from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib
import base64
def encrypt_blob(blob, public_key):
    rsa_public_key = RSA.import_key(public_key)
    rsa_cipher = PKCS1_OAEP.new(rsa_public_key)
    compressed_blob = zlib.compress(blob)
    chunk_size = 470
    encrypted_data = b""
    for offset in range(0, len(compressed_blob), chunk_size):
        chunk = compressed_blob[offset:offset + chunk_size]
        if len(chunk) < chunk_size:
            padding = b" " * (chunk_size - len(chunk))
            chunk += padding
        encrypted_data += rsa_cipher.encrypt(chunk)
    return base64.b64encode(encrypted_data)
with open("TA_public_key.pem", "rb") as public_key_file:
    rsa_public_key = public_key_file.read()
with open("rootbeer.jpg", "rb") as image_file:
    unencrypted_blob = image_file.read()
encrypted_blob = encrypt_blob(unencrypted_blob, rsa_public_key)
with open("encrypted_img.jpg", "wb") as encrypted_image_file:
    encrypted_image_file.write(encrypted_blob)
    print('Stored encrypted image to', encrypted_image_file.name)