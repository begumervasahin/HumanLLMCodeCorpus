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
def get_padding(secret):
    pl = len(secret)
    mod = pl % 16
    if mod != 0:
        padding = 16 - mod
        secret += 'X' * padding
    return secret
def byte_to_hex(elt):
    return binascii.hexlify(elt)
def disp(message, target, encrypted, see_oracle):
    if see_oracle:
        print("\nMessage to encrypt: ", message)
    else:
        print("\nMessage to encrypt: ?")
    print("Target given: ", target)
    if see_oracle:
        for i in range(0, len(message), 16):
            print("Message Split", message[i:i+16], end=" ")
        print("\nSecret we don't know:", token)
        print("\tEncrypting with AES-ECB.... \n\tKey =", binascii.hexlify(key))
    else:
        for i in range(0, len(message), 16):
            print("Message Split", "?" * 16, end=" ")
    print("\nEncrypted:", byte_to_hex(encrypted), "\n\n")
def oracle(target, display=False, see_oracle=False, timing=False):
    message = get_padding("data=" + target + ",token=" + token)
    message_encoded = message.encode()
    encrypted = encrypt(message_encoded)
    if display:
        if timing: time.sleep(.05)
        disp(message, target, encrypted, see_oracle)
    encrypted_decoded = byte_to_hex(encrypted)
    print("Encrypted decoded", encrypted_decoded)
    return encrypted
if __name__ == "__main__":
    target = "exampledata"
    oracle(target, display=True, see_oracle=True, timing=True)