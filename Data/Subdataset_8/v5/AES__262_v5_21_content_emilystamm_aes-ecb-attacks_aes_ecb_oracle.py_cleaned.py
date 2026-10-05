from Crypto.Cipher import AES
import binascii
import time
from Crypto.Random import get_random_bytes
def generate_aes_key(length=16):
    return get_random_bytes(length)
def initialize_cipher(key):
    return AES.new(key, AES.MODE_ECB)
def encrypt_message(cipher, message):
    return cipher.encrypt(message)
def pad_message(data, block_size=16):
    padding_length = (block_size - len(data) % block_size) % block_size
    return data + 'X' * padding_length
def display_encryption_process(message, target, encrypted, reveal, key):
    print("\nMessage to encrypt:", message if reveal else "?")
    print("Target given:", target)
    if reveal:
        print("\nSecret token:", token)
        print("\tEncrypting with AES-ECB...\n\tKey:", binascii.hexlify(key).decode())
    else:
        print("\nDetails are hidden.")
    print("\nEncrypted (hex):", binascii.hexlify(encrypted).decode(), "\n")
def encryption_oracle(target, key, cipher, display=False, reveal=False, timing=False):
    padded_message = pad_message(f"data={target},token={token}")
    encrypted = encrypt_message(cipher, padded_message.encode())
    if display:
        if timing: time.sleep(0.05)
        display_encryption_process(padded_message, target, encrypted, reveal, key)
    return binascii.hexlify(encrypted).decode()
key = generate_aes_key()
cipher = initialize_cipher(key)
token = "VERYsecrettokn1"
print("Key:", binascii.hexlify(key).decode())
if __name__ == "__main__":
    target_example = "exampledata"
    encrypted_output = encryption_oracle(target_example, key, cipher, display=True, reveal=True, timing=True)
    print("Encrypted output:", encrypted_output)