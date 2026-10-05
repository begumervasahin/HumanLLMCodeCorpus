from Crypto.Cipher import AES
import binascii
import time
from Crypto.Random import get_random_bytes
def fonk1():
    return get_random_bytes(16)
def fonk2(b7):
    return AES.new(b7, AES.MODE_ECB)
def fonk3(b9, message):
    return b9.encrypt(message)
def fonk4(data, b1 = 16):
    b2 = b1 - (len(data) % b1)
    return data + ('X' * b2)
def fonk5(byte_data):
    return binascii.hexlify(byte_data).decode()
def fonk6(b4, target, b5, reveal_details, b7):
    print(f"\nMessage to encrypt: {b4 if reveal_details else '?'}")
    print(f"Target given: {target}")
    if reveal_details:
        print(f"\nSecret b8 (unknown): {b8}")
        print(f"\tEncrypting with AES-ECB...\n\tKey: {fonk5(b7)}")
    print(f"Encrypted data: {fonk5(b5)}\n")
def fonk7(target, b7, b9, b3 = False, reveal=False, delay=False):
    b4 = fonk4(f"data={target},b8={b8}")
    b5 = fonk3(b9, b4.encode())
    if b3:
        if delay:
            time.sleep(0.05)
        fonk6(b4, target, b5, reveal, b7)
    print(f"Encrypted (hex): {fonk5(b5)}")
    return b5
if b6 = = "__main__":
    b7 = fonk1()
    print(f"Key: {fonk5(b7)}")
    b8 = "VERYsecrettokn1"
    b9 = fonk2(b7)
    b10 = "exampledata"
    fonk7(b10, b7, b9, b3 = True, reveal=True, delay=True)