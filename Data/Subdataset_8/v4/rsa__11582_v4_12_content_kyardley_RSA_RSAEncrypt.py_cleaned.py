import zlib
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
def encrypt_blob(blob, public_key):
    rsa_key = RSA.importKey(public_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)
    blob = zlib.compress(blob)
    chunk_size = 470
    offset = 0
    end_loop = False
    encrypted = b''
    while not end_loop:
        chunk = blob[offset:offset + chunk_size]
        if len(chunk) % chunk_size != 0:
            end_loop = True
            chunk += b" " * (chunk_size - len(chunk))
        encrypted += rsa_key.encrypt(chunk)
        offset += chunk_size
    encoded_encrypted = base64.b64encode(encrypted)
    return encoded_encrypted
with open("TA_public_key.pem", "rb") as fd:
    public_key = fd.read()
with open("rootbeer.jpg", "rb") as fd:
    unencrypted_blob = fd.read()
encrypted_blob = encrypt_blob(unencrypted_blob, public_key)
with open("encrypted_img.jpg", "wb") as fd:
    fd.write(encrypted_blob)
    print('Stored encrypted image to', fd.name)