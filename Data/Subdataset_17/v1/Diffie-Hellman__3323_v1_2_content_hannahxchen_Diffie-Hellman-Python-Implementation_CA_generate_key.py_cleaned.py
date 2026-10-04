from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
def generate_rsa_key_pair(bits=1024):
    key = RSA.generate(bits, get_random_bytes)
    private_key = key
    public_key = key.publickey()
    return private_key, public_key
def save_key_to_file(filename, key):
    with open(filename, "wb") as file:
        file.write(key.export_key())
def main():
    private_key1, public_key1 = generate_rsa_key_pair()
    private_key2, public_key2 = generate_rsa_key_pair()
    save_key_to_file("privatekey1.pem", private_key1)
    save_key_to_file("publickey1.pem", public_key1)
    save_key_to_file("privatekey2.pem", private_key2)
    save_key_to_file("publickey2.pem", public_key2)
    print("Finished generating key pairs")
if __name__ == "__main__":
    main()