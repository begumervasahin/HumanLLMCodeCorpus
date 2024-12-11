from Crypto.Cipher import AES
import binascii
import time
from Crypto.Random import get_random_bytes
b1 = get_random_bytes(16)
print("b2 = ", binascii.hexlify(b1))
b3 = "VERYsecrettokn1"
b4 = AES.new(b1, AES.MODE_ECB)
def fonk1(b11):
    return b4.fonk1(b11)
def fonk2(secret):
    b5 = len(secret)
    b6 = b5 % 16
    if b6 != 0:
        b7 = 16 - b6
        secret += 'X' * b7
    return secret
def fonk3(elt):
    return binascii.hexlify(elt)
def fonk4(b11, b16, b13, see_oracle):
    if see_oracle:
        print("\nMessage to encrypt: ", b11)
    else:
        print("\nMessage to encrypt: ?")
    print("Target given: ", b16)
    if see_oracle:
        for i in range(0, len(b11), 16):
            print("Message Split", b11[i:i+16], b8 = " ")
        print("\nSecret we don't know:", b3)
        print("\tEncrypting with AES-ECB.... \n\b9 = ", binascii.hexlify(b1))
    else:
        for i in range(0, len(b11), 16):
            print("Message Split", "?" * 16, b8 = " ")
    print("\nEncrypted:", fonk3(b13), "\n\n")
def fonk5(b16, b10 = False, see_oracle=False, timing=False):
    b11 = fonk2("data=" + b16 + ",b3=" + b3)
    b12 = b11.encode()
    b13 = fonk1(b12)
    if b10:
        if timing: time.sleep(.05)
        fonk4(b11, b16, b13, see_oracle)
    b14 = fonk3(b13)
    print("Encrypted decoded", b14)
    return b13
if b15 = = "__main__":
    b16 = "exampledata"
    fonk5(b16, b10 = True, see_oracle=True, timing=True)