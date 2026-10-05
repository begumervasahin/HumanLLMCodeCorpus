from Crypto.Cipher import AES
import binascii
import time
from Crypto.Random import get_random_bytes
key = get_random_bytes(16)
print("Key = ", binascii.hexlify(key))
token = "VERYsecrettokn1"
cipher = AES.new(key, AES.MODE_ECB)
def encrypt(message):
    return cipher.encrypt(message)
def get_padded_message(data):
    padding_length = 16 - (len(data) % 16)
    if padding_length != 16:
        data += 'X' * padding_length
    return data
def bytes_to_hex(bytes_data):
    return binascii.hexlify(bytes_data)
def display_encryption_details(message, target, encrypted, reveal):
    if reveal:
        print("\nMessage to encrypt: ", message)
        print("Secret we don't know:", token)
    else:
        print("\nMessage to encrypt: ?")
    print("Target given: ", target)
    if reveal:
        for i in range(0, len(message), 16):
            print("Message Split", message[i:i+16], end=" ")
        print("\n\tEncrypting with AES-ECB.... \n\tKey =", binascii.hexlify(key))
    else:
        for i in range(0, len(message), 16):
            print("Message Split", "?" * 16, end=" ")
    print("\nEncrypted:", bytes_to_hex(encrypted), "\n")
def encryption_oracle(target, display=False, reveal=False, timing=False):
    message = get_padded_message("data=" + target + ",token=" + token)
    message_encoded = message.encode()
    encrypted = encrypt(message_encoded)
    if display:
        if timing:
            time.sleep(0.05)
        display_encryption_details(message, target, encrypted, reveal)
    encrypted_decoded = bytes_to_hex(encrypted)
    print("Encrypted decoded", encrypted_decoded)
    return encrypted
if __name__ == "__main__":
    target_example = "exampledata"
    encryption_oracle(target_example, display=True, reveal=True, timing=True)