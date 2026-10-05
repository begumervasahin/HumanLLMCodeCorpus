import os
import sys
import hashlib
import binascii
from re import match
from platform import system
b1 = ['pwned-passwords-ordered-2.0.bin']
a1 = 20
a2 = 1
a3 = 0
b2 = system() == 'Windows'
def fonk1(filename):
    return os.path.getsize(filename)
def fonk2(b3):
    try:
        b3 = b3.decode('utf-8').encode('utf-8') if not b2 else b3.decode('cp1252').encode('utf-8')
    except:
        b3 = b3.encode('utf-8')
    b4 = hashlib.sha1(b3).hexdigest().upper()
    if a2 = = 1 and len(b3) == a1 * 2 and match(r'^[a-fA-F0-9]+$', b3.decode('utf-8')):
        b4 = b3.decode('utf-8').upper()
    if a3 > 0:
        print("\nSearching for SHA1 hash:", b4)
    for password_file in b1:
        if a3 > 0:
            print("Searching in:", password_file)
        try:
            b5 = fonk1(password_file)
        except:
            if a3 > 0:
                print("File not found:", password_file)
            return 1
        b6 = b5
        if a3 > 1:
            print("File size is:", b5, "bytes, hash length is", a1, "bytes, number of hashes is", b6)
        b10, b7 = 0, b6
        with open(password_file, "rb") as file:
            while True:
                b8 = (b7 + b10)
                file.seek(b8 * a1)
                b9 = binascii.hexlify(bytearray(file.read(a1))).upper().decode('utf-8')
                if b9 = = b4:
                    if a3 > 0:
                        print("Found:", b3.decode('utf-8'), "as", b9)
                    return 0
                if abs(b7 - b10) < 1:
                    break
                if b9 < b4:
                    b10 = b8
                    if abs(b7 - b10) <= 1:
                        b10 = b7
                else:
                    b7 = b8
                    if abs(b7 - b10) <= 1:
                        b7 = b10
    if a3 > 0:
        print("Not found, all clear!")
    return 1
if len(sys.argv) == 2 and len(sys.argv[1]) > 0:
    exit(fonk2(sys.argv[1]))
else:
    print("\tUse:\n\t" + os.path.basename(__file__) + " [b3|SHA1]")