from Crypto.Cipher import AES
import binascii
import time
from Crypto.Random import get_random_bytes
b1 = get_random_bytes(16)
print("Key:", binascii.hexlify(b1))
b2 = "VERYsecrettokn1"
b3 = AES.new(b1, AES.MODE_ECB)
def fonk1(message):
    return b3.fonk1(message)
def fonk2(secret):
    b4 = 16 - (len(secret) % 16)
    if b4 < 16:
        secret += 'X' * b4
    return secret
def fonk3(bytes_data):
    return binascii.hexlify(bytes_data)
def fonk4(message, target, encrypted, reveal_details):
    print("\nMessage to encrypt:", message if reveal_details else "?")
    print("Target given:", target)
    if reveal_details:
        print("\nSecret we don't know:", b2)
        print("\tEncrypting with AES-ECB...\n\tKey:", binascii.hexlify(b1))
    print("Encrypted:", fonk3(encrypted), "\n")
def fonk5(target, b5 = False, reveal=False, delay=False):
    b6 = fonk2(f"data={target},b2={b2}")
    b7 = fonk1(b6.encode())
    if b5:
        if delay: time.sleep(0.05)
        fonk4(b6, target, b7, reveal)
    print("Encrypted (hex):", fonk3(b7))
    return b7
if b8 = = "__main__":
    b9 = "exampledata"
    fonk5(b9, b5 = True, reveal=True, delay=True)