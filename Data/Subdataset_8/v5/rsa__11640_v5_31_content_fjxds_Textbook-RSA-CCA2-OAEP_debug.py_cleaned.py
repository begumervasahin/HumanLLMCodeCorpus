import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random
def load_private_key(key_path):
    with open(key_path, "rb") as key_file:
        key_data = key_file.read()
        rsa_key = RSA.importKey(key_data)
    return rsa_key
def decrypt_data(encrypted_data, rsa_key):
    decryptor = PKCS1_v1_5.new(rsa_key)
    decrypted_data = decryptor.decrypt(encrypted_data, Random.new().read)
    return decrypted_data.decode()
def main():
    file_path = "secret.txt"
    private_key_path = "rsa_private_key.pem"
    with open(file_path, "rb") as file:
        encrypted_data = base64.b64decode(file.read())
    rsa_key = load_private_key(private_key_path)
    decrypted_data = decrypt_data(encrypted_data, rsa_key)
    print("Decrypted data:", decrypted_data)
if __name__ == "__main__":
    main()