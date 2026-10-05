from Crypto.Cipher import AES
import binascii
import time
from Crypto.Random import get_random_bytes
key = get_random_bytes(16)
print("Key:", binascii.hexlify(key))
token = "VERYsecrettokn1"
cipher = AES.new(key, AES.MODE_ECB)
def encrypt(message):
    return cipher.encrypt(message)
def get_padding(secret):
    padding_length = 16 - (len(secret) % 16)
    if padding_length < 16:
        secret += 'X' * padding_length
    return secret
def bytes_to_hex(bytes_data):
    return binascii.hexlify(bytes_data)
def display_info(message, target, encrypted, reveal_details):
    print("\nMessage to encrypt:", message if reveal_details else "?")
    print("Target given:", target)
    if reveal_details:
        print("\nSecret we don't know:", token)
        print("\tEncrypting with AES-ECB...\n\tKey:", binascii.hexlify(key))
    print("Encrypted:", bytes_to_hex(encrypted), "\n")
def encryption_oracle(target, show=False, reveal=False, delay=False):
    padded_message = get_padding(f"data={target},token={token}")
    encrypted_message = encrypt(padded_message.encode())
    if show:
        if delay: time.sleep(0.05)
        display_info(padded_message, target, encrypted_message, reveal)
    print("Encrypted (hex):", bytes_to_hex(encrypted_message))
    return encrypted_message
if __name__ == "__main__":
    example_target = "exampledata"
    encryption_oracle(example_target, show=True, reveal=True, delay=True)