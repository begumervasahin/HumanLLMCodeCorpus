import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random
random_generator = Random.new().read
file_path = "secret.txt"
with open(file_path, "rb") as f:
    encrypted_data = f.read()
    decoded_data = base64.b64decode(encrypted_data)
    print(decoded_data)
private_key_path = "rsa_private_key.pem"
default_length = 117
with open(private_key_path, "rb") as f:
    key_data = f.read()
    rsa_key = RSA.importKey(key_data)
    decryptor = PKCS1_v1_5.new(rsa_key)
    decrypted_data = decryptor.decrypt(decoded_data, random_generator)
    print(decrypted_data.decode())
