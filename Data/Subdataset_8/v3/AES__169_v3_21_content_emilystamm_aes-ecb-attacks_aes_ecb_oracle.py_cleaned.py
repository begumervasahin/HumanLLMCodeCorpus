from Crypto.Cipher import AES
import binascii
import time
from Crypto.Random import get_random_bytes
def generate_aes_key():
    return get_random_bytes(16)
def initialize_cipher(key):
    return AES.new(key, AES.MODE_ECB)
def encrypt_message(cipher, message):
    return cipher.encrypt(message)
def apply_padding(data, block_size=16):
    padding_needed = block_size - (len(data) % block_size)
    return data + ('X' * padding_needed)
def convert_bytes_to_hex(byte_data):
    return binascii.hexlify(byte_data).decode()
def display_encryption_details(padded_message, target, encrypted_data, reveal_details, key):
    print(f"\nMessage to encrypt: {padded_message if reveal_details else '?'}")
    print(f"Target given: {target}")
    if reveal_details:
        print(f"\nSecret token (unknown): {token}")
        print(f"\tEncrypting with AES-ECB...\n\tKey: {convert_bytes_to_hex(key)}")
    print(f"Encrypted data: {convert_bytes_to_hex(encrypted_data)}\n")
def encryption_oracle(target, key, cipher, show=False, reveal=False, delay=False):
    padded_message = apply_padding(f"data={target},token={token}")
    encrypted_data = encrypt_message(cipher, padded_message.encode())
    if show:
        if delay:
            time.sleep(0.05)
        display_encryption_details(padded_message, target, encrypted_data, reveal, key)
    print(f"Encrypted (hex): {convert_bytes_to_hex(encrypted_data)}")
    return encrypted_data
if __name__ == "__main__":
    key = generate_aes_key()
    print(f"Key: {convert_bytes_to_hex(key)}")
    token = "VERYsecrettokn1"
    cipher = initialize_cipher(key)
    example_target = "exampledata"
    encryption_oracle(example_target, key, cipher, show=True, reveal=True, delay=True)