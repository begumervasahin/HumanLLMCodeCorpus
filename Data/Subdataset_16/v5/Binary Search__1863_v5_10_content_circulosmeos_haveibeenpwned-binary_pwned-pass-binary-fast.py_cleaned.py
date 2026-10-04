import os
import hashlib
import sys
import binascii
from re import match
from platform import system
b1 = ['pwned-passwords-ordered-2.0.bin']
a1 = 20
b2 = True
b3 = False
b4 = system() == 'Windows'
def fonk1(filename):
    return os.path.getsize(filename)
def fonk2(b5):
    return b2 and len(b5) == a1 * 2 and match(r'^[a-fA-F0-9]+$', b5.decode('utf-8'))
def fonk3(b5):
    try:
        if b4:
            return b5.decode('cp1252').encode('utf-8')
        return b5.decode('utf-8').encode('utf-8')
    except AttributeError:
        return b5.encode('utf-8')
def fonk4(b5):
    b5 = fonk3(b5)
    b6 = hashlib.sha1(b5).hexdigest().upper()
    if fonk2(b5):
        b6 = b5.decode('utf-8').upper()
    if b3:
        print(f"\nSearching for SHA1 hash: {b6}")
    for password_file in b1:
        if b3:
            print(f"Searching in: {password_file}")
        try:
            b7 = fonk1(password_file)
        except FileNotFoundError:
            if b3:
                print(f"File not found: {password_file}")
            return 1
        b8 = b7
        if b3:
            print(f"File size: {b7} bytes, hash length: {a1} bytes, number of hashes: {b8}")
        b12, b9 = 0, b8
        with open(password_file, "rb") as file:
            while b12 < b9:
                b10 = (b9 + b12)
                file.seek(b10 * a1)
                b11 = binascii.hexlify(file.read(a1)).upper().decode('utf-8')
                if b3:
                    print(f"Checking hash position {b10}: {b11}")
                if b11 = = b6:
                    if b3:
                        print(f"Found: '{b5.decode('utf-8')}' as {b11}")
                    return 0
                elif b11 < b6:
                    b12 = b10 + 1
                else:
                    b9 = b10
    if b3:
        print("Not found, all clear!")
    return 1
def fonk5():
    if len(sys.argv) == 2 and sys.argv[1]:
        sys.exit(fonk4(sys.argv[1]))
    else:
        b13 = os.path.basename(__file__)
        print(f"Usage:\n\t{b13} [b5|SHA1]")
if b14 = = "__main__":
    fonk5()