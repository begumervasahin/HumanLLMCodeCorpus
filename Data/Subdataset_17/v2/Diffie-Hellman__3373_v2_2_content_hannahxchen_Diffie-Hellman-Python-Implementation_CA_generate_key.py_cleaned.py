from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
def generate_rsa_key_pair(bits=1024):
    key = RSA.generate(bits, get_random_bytes)
    private_key = key
    public_key = key.publickey()
    return private_key, public_key
def save_key_to_file(file_path, key):
    with open(file_path, "wb") as file:
        file.write(key.export_key())
def main():
    private_key1, public_key1 = generate_rsa_key_pair()
    private_key2, public_key2 = generate_rsa_key_pair()
    private_key1_path = "privatekey1.pem"
    public_key1_path = "publickey1.pem"
    private_key2_path = "privatekey2.pem"
    public_key2_path = "publickey2.pem"
    save_key_to_file(private_key1_path, private_key1)
    save_key_to_file(public_key1_path, public_key1)
    save_key_to_file(private_key2_path, private_key2)
    save_key_to_file(public_key2_path, public_key2)
    print("Key pairs generated and saved successfully.")
if __name__ == "__main__":
    main()