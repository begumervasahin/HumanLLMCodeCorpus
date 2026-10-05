from Crypto.Cipher import AES
import binascii
import time
from Crypto.Random import get_random_bytes
def fonk1(b1 = 16):
    return get_random_bytes(b1)
def fonk2(b7):
    return AES.new(b7, AES.MODE_ECB)
def fonk3(b8, message):
    return b8.encrypt(message)
def fonk4(data, b2 = 16):
    b3 = (b2 - len(data) % b2) % b2
    return data + 'X' * b3
def fonk5(message, target, b6, reveal, b7):
    print("\nMessage to encrypt:", message if reveal else "?")
    print("Target given:", target)
    if reveal:
        print("\nSecret b9:", b9)
        print("\tEncrypting with AES-ECB...\n\tKey:", binascii.hexlify(b7).decode())
    else:
        print("\nDetails are hidden.")
    print("\nEncrypted (hex):", binascii.hexlify(b6).decode(), "\n")
def fonk6(target, b7, b8, b4 = False, reveal=False, timing=False):
    b5 = fonk4(f"data={target},b9={b9}")
    b6 = fonk3(b8, b5.encode())
    if b4:
        if timing: time.sleep(0.05)
        fonk5(b5, target, b6, reveal, b7)
    return binascii.hexlify(b6).decode()
b7 = fonk1()
b8 = fonk2(b7)
b9 = "VERYsecrettokn1"
print("Key:", binascii.hexlify(b7).decode())
if b10 = = "__main__":
    b11 = "exampledata"
    b12 = fonk6(b11, b7, b8, b4=True, reveal=True, timing=True)
    print("Encrypted output:", b12)