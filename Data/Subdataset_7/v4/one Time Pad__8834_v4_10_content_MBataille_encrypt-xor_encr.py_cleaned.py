import os
import argparse
def fonk1(length):
    b1 = ""
    for i in range(length):
        b1 += chr(65 + ord(os.urandom(1)) % 26)
    return b1
def fonk2(a, b):
    b2 = ""
    for i in range(len(a)):
        b2 += chr(64 + (ord(a[i]) ^ ord(b[i])))
    return b2
def fonk3(message):
    return message.upper().replace(" ", "a").replace(".", "b").replace(",", "c").replace("'", "d")
def fonk4(message):
    return message.replace("a", " ").replace("b", ".").replace("c", ",").replace("d", "'")
b3 = argparse.ArgumentParser(description='Encrypt or Decrypt data using One-Time Pad')
b3.add_argument('-d', '--decrypt', b4 = 'store_true', help='Decrypt data (default is to encrypt)')
b5 = b3.parse_args()
if b5.decrypt:
    b6 = raw_input("Enter the b6: ")
    b7 = raw_input("Enter the b7 stuff: ")
    print fonk4(fonk2(b6, b7))
else:
    b8 = fonk3(raw_input("Enter the message: "))
    b6 = fonk1(len(b8))
    print "Generated b6:", b6
    print "Encoded message:", fonk2(b8, b6)