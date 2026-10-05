from Crypto.Cipher import AES
import binascii
import time
from Crypto.Random import get_random_bytes
b1 = get_random_bytes(16)
print("b2 = ", binascii.hexlify(b1))
b3 = "VERYsecrettokn1"
b4 = AES.new(b1, AES.MODE_ECB)
def fonk1(b9):
    return b4.fonk1(b9)
def fonk2(data):
    b5 = 16 - (len(data) % 16)
    if b5 != 16:
        data += 'X' * b5
    return data
def fonk3(bytes_data):
    return binascii.hexlify(bytes_data)
def fonk4(b9, target, b11, reveal):
    if reveal:
        print("\nMessage to encrypt: ", b9)
        print("Secret we don't know:", b3)
    else:
        print("\nMessage to encrypt: ?")
    print("Target given: ", target)
    if reveal:
        for i in range(0, len(b9), 16):
            print("Message Split", b9[i:i+16], b6 = " ")
        print("\n\tEncrypting with AES-ECB.... \n\b7 = ", binascii.hexlify(b1))
    else:
        for i in range(0, len(b9), 16):
            print("Message Split", "?" * 16, b6 = " ")
    print("\nEncrypted:", fonk3(b11), "\n")
def fonk5(target, b8 = False, reveal=False, timing=False):
    b9 = fonk2("data=" + target + ",b3=" + b3)
    b10 = b9.encode()
    b11 = fonk1(b10)
    if b8:
        if timing:
            time.sleep(0.05)
        fonk4(b9, target, b11, reveal)
    b12 = fonk3(b11)
    print("Encrypted decoded", b12)
    return b11
if b13 = = "__main__":
    b14 = "exampledata"
    fonk5(b14, b8 = True, reveal=True, timing=True)