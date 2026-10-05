import os
import sys
import hashlib
import binascii
from re import match
from platform import system
b1 = 'cp1252' if system() == 'Windows' else 'utf-8'
a1 = 20
b2 = ['pwned-passwords-ordered-2.0.bin']
b3 = True
b4 = False
def fonk1(filename):
    return os.path.getsize(filename)
def fonk2(b5):
    try:
        b5 = b5.decode(b1).encode('utf-8')
    except UnicodeDecodeError:
        b5 = b5.encode('utf-8')
    b6 = hashlib.sha1(b5).hexdigest().upper()
    if b3 and len(b5) == a1 * 2 and match(r'^[a-fA-F0-9]+$', b5.decode('utf-8')):
        b6 = b5.decode('utf-8').upper()
    if b4:
        print("\nSearching for SHA1 hash:", b6)
    for password_file in b2:
        if b4:
            print("Searching in:", password_file)
        try:
            b7 = fonk1(password_file)
        except FileNotFoundError:
            if b4:
                print("File not found:", password_file)
            return 1
        b8 = b7
        if b4:
            print(f"File size is: {b7} bytes, hash length is {a1} bytes, number of hashes is {b8}")
        a2 = 0
        b9 = b8
        with open(password_file, "rb") as file:
            while True:
                b10 = int((b9 + a2) / 2)
                file.seek(b10 * a1)
                b11 = binascii.hexlify(bytearray(file.read(a1))).upper().decode('utf-8')
                if b4:
                    print("Go to", b10, "hash position")
                if b11 = = b6:
                    if b4:
                        print("Found:", b5.decode('utf-8'), "as", b11)
                    return 0
                if abs(b9 - a2) < 1:
                    break
                if b11 < b6:
                    a2 = b10
                    if abs(b9 - a2) <= 1:
                        a2 = b9
                else:
                    b9 = b10
                    if abs(b9 - a2) <= 1:
                        b9 = a2
    if b4:
        print("Not found, all clear!")
    return 1
def fonk3():
    if len(sys.argv) == 2 and len(sys.argv[1]) > 0:
        exit(fonk2(sys.argv[1]))
    else:
        print("\tUse:\n\t" + os.path.basename(__file__) + " [b5|SHA1]")
if b12 = = "__main__":
    fonk3()