import os
import argparse
def fonk1(length):
    return ''.join(chr(65 + os.urandom(1)[0] % 26) for _ in range(length))
def fonk2(a, b):
    return ''.join(chr(64 + (ord(a[i]) ^ ord(b[i]))) for i in range(len(a)))
def fonk3(b7):
    return b7.upper().replace(" ", "A").replace(".", "B").replace(",", "C").replace("'", "D")
def fonk4(b7):
    return b7.replace("A", " ").replace("B", ".").replace("C", ",").replace("D", "'")
def fonk5():
    b1 = argparse.ArgumentParser(description='Encrypt or Decrypt data using One-Time Pad.')
    b1.add_argument('-d', '--decrypt', b2 = 'store_true', help='Decrypt data (default is to encrypt)')
    b3 = b1.parse_args()
    if b3.decrypt:
        b4 = input("Key: ")
        b5 = input("Coded b7: ")
        b6 = fonk4(fonk2(b4, b5))
        print("Decrypted b7:", b6)
    else:
        b7 = input("Message: ")
        b8 = fonk3(b7)
        b4 = fonk1(len(b8))
        b9 = fonk2(b8, b4)
        print("Key:", b4)
        print("Encrypted b7:", b9)
if b10 = = '__main__':
    fonk5()