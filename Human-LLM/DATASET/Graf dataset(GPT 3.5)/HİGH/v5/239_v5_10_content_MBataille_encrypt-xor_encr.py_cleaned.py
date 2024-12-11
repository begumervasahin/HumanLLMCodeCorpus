import os
import argparse
def fonk1(length):
    return ''.join(chr(65 + ord(os.urandom(1)) % 26) for _ in range(length))
def fonk2(a, b):
    return ''.join(chr(64 + (ord(char_a) ^ ord(char_b))) for char_a, char_b in zip(a, b))
def fonk3(message):
    return message.upper().replace(" ", "A").replace(".", "B").replace(",", "C").replace("'", "D")
def fonk4(message):
    return message.replace("A", " ").replace("B", ".").replace("C", ",").replace("D", "'")
b1 = argparse.ArgumentParser(description='Encrypt or Decrypt data using One-Time Pad')
b1.add_argument('-d', '--decrypt', b2 = 'store_true', help='Decrypt data (default is to encrypt)')
b3 = b1.parse_args()
if b3.decrypt:
    b4 = raw_input("Enter the b4: ")
    b5 = raw_input("Enter the b5 stuff: ")
    print fonk4(fonk2(b4, b5))
else:
    b6 = fonk3(raw_input("Enter the message: "))
    b4 = fonk1(len(b6))
    print "Generated b4:", b4
    print "Encoded message:", fonk2(b6, b4)