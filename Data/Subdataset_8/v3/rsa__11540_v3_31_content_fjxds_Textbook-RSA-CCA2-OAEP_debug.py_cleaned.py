import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random
import rsa
def load_encrypted_data(file_path):
    with open(file_path, "rb") as file:
        return file.read()
def decode_base64(data):
    return base64.b64decode(data)
def load_private_key(private_key_path):
    with open(private_key_path, "rb") as key_file:
        private_key_data = key_file.read()
        return RSA.importKey(private_key_data)
def decrypt_with_crypto(decoded_data, rsa_key):
    decryptor = PKCS1_v1_5.new(rsa_key)
    return decryptor.decrypt(decoded_data, Random.new().read)
def decrypt_with_rsa(decoded_data, private_key_rsa):
    return rsa.decrypt(decoded_data, private_key_rsa)
def main():
    encrypted_data = load_encrypted_data("secret.txt")
    decoded_data = decode_base64(encrypted_data)
    rsa_key = load_private_key("rsa_private_key.pem")
    decrypted_data_crypto = decrypt_with_crypto(decoded_data, rsa_key)
    print("Decrypted using Crypto module PKCS1_v1_5:", decrypted_data_crypto)
    private_key_rsa = rsa.PrivateKey.load_pkcs1(rsa_key.export_key())
    decrypted_data_rsa = decrypt_with_rsa(decoded_data, private_key_rsa)
    print("Decrypted using rsa module:", decrypted_data_rsa)
if __name__ == "__main__":
    main()