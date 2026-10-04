from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
def generate_rsa_key(bits=1024):
    key = RSA.generate(bits, get_random_bytes)
    return key, key.publickey()
def save_key_to_file(file_path, key):
    with open(file_path, "wb") as file:
        file.write(key.export_key())
def main():
    private_key1, public_key1 = generate_rsa_key()
    private_key2, public_key2 = generate_rsa_key()
    key_file_paths = {
        "private_key1": "privatekey1.pem",
        "public_key1": "publickey1.pem",
        "private_key2": "privatekey2.pem",
        "public_key2": "publickey2.pem"
    }
    save_key_to_file(key_file_paths["private_key1"], private_key1)
    save_key_to_file(key_file_paths["public_key1"], public_key1)
    save_key_to_file(key_file_paths["private_key2"], private_key2)
    save_key_to_file(key_file_paths["public_key2"], public_key2)
    print("RSA key pairs have been generated and saved successfully.")
if __name__ == "__main__":
    main()