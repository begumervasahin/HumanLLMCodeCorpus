from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
def generate_key_pair():
    random_generator = Random.new().read
    key_pair = RSA.generate(1024, random_generator)
    return key_pair, key_pair.publickey()
def encrypt_message(public_key, message):
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message
def decrypt_message(private_key, encrypted_message):
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()
def main():
    private_key, public_key = generate_key_pair()
    plain_text = "Hello World"
    encrypted_text = encrypt_message(public_key, plain_text)
    print("Encrypted Text:", encrypted_text)
    decrypted_text = decrypt_message(private_key, encrypted_text)
    print("Decrypted Text:", decrypted_text)
if __name__ == "__main__":
    main()