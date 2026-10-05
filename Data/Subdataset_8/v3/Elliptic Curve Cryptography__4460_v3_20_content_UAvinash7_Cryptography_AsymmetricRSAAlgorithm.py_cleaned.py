from Crypto.PublicKey import RSA
from Crypto import Random
import ast
def generate_key_pair():
    random_generator = Random.new().read
    return RSA.generate(1024, random_generator)
def encrypt_message(public_key, message):
    return public_key.encrypt(message.encode(), 32)
def decrypt_message(key_pair, encrypted_text):
    return key_pair.decrypt(ast.literal_eval(str(encrypted_text))).decode()
def main():
    key_pair = generate_key_pair()
    public_key = key_pair.publickey()
    plain_text = "Hello World"
    encrypted_text = encrypt_message(public_key, plain_text)
    print("Encrypted Text:", encrypted_text)
    decrypted_text = decrypt_message(key_pair, encrypted_text)
    print("Decrypted Text:", decrypted_text)
if __name__ == "__main__":
    main()