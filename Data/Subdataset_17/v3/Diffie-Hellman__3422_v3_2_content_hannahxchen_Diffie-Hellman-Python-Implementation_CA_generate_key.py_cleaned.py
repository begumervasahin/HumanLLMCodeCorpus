from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
def generate_rsa_key_pair(bits=1024):
    key = RSA.generate(bits, get_random_bytes)
    return key, key.publickey()
def save_key_to_file(file_path, key):
    with open(file_path, "wb") as file:
        file.write(key.export_key())
def main():
    private_key1, public_key1 = generate_rsa_key_pair()
    private_key2, public_key2 = generate_rsa_key_pair()
    file_paths = {
        "privatekey1": "privatekey1.pem",
        "publickey1": "publickey1.pem",
        "privatekey2": "privatekey2.pem",
        "publickey2": "publickey2.pem"
    }
    save_key_to_file(file_paths["privatekey1"], private_key1)
    save_key_to_file(file_paths["publickey1"], public_key1)
    save_key_to_file(file_paths["privatekey2"], private_key2)
    save_key_to_file(file_paths["publickey2"], public_key2)
    print("Key pairs generated and saved successfully.")
if __name__ == "__main__":
    main()