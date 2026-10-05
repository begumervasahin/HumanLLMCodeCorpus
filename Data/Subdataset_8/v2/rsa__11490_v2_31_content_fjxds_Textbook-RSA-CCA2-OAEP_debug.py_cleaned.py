import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random
import rsa
file_path = "secret.txt"
with open(file_path, "rb") as file:
    encrypted_data = file.read()
decoded_data = base64.b64decode(encrypted_data)
private_key_path = "rsa_private_key.pem"
with open(private_key_path, "rb") as key_file:
    private_key_data = key_file.read()
    rsa_key = RSA.importKey(private_key_data)
decryptor = PKCS1_v1_5.new(rsa_key)
decrypted_data_crypto = decryptor.decrypt(decoded_data, Random.new().read)
print("Decrypted using Crypto module PKCS1_v1_5:", decrypted_data_crypto)
private_key_rsa = rsa.PrivateKey.load_pkcs1(private_key_data)
decrypted_data_rsa = rsa.decrypt(decoded_data, private_key_rsa)
print("Decrypted using rsa module:", decrypted_data_rsa)