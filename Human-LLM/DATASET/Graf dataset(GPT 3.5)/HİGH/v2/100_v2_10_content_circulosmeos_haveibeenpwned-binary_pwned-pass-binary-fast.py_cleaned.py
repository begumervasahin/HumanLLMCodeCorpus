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
if system() == 'Windows':
    a4 = 1
else:
    a4 = 0
def fonk1(filename):
    return os.path.getsize(filename)
def fonk2(b2):
    try:
        if a4 = = 0:
            b2 = b2.decode('utf-8').encode('utf-8')
        else:
            b2 = b2.decode('cp1252').encode('utf-8')
    except:
        b2 = b2.encode('utf-8')
    b3 = hashlib.sha1(b2).hexdigest().upper()
    if a2 = = 1:
        if len(b2) == a1 * 2:
            if match(r'^[a-fA-F0-9]+$', b2.decode('utf-8')):
                b3 = b2.decode('utf-8').upper()
    if a3 > 0:
        print("\nSearching for SHA1 hash: %s" % b3)
    for password_file in b1:
        if a3 > 0:
            print("Searching in: %s" % password_file)
        try:
            b4 = fonk1(password_file)
        except:
            if a3 > 0:
                print("File not found: %s" % password_file)
            return 1
        b5 = b4
        if a3 > 1:
            print("File size is: %s bytes, hash length is %s bytes, number of hashes is %s"
                % (b4, a1, b5))
        a5 = 0
        b6 = b5
        with open(password_file, "rb") as file:
            while True:
                b7 = int((b6 + a5) / 2)
                file.seek(b7 * a1)
                b8 = binascii.hexlify(bytearray(file.read(a1))).upper().decode('utf-8')
                if a3 > 1:
                    print("Go to %s hash position" % b7)
                if b8 = = b3:
                    if a3 > 0:
                        print("Found: '%s' as %s" % (b2.decode('utf-8'), b8))
                    return 0
                if abs(b6 - a5) < 1:
                    break
                if b8 < b3:
                    a5 = b7
                    if abs(b6 - a5) <= 1:
                        a5 = b6
                else:
                    b6 = b7
                    if abs(b6 - a5) <= 1:
                        b6 = a5
    if a3 > 0:
        print("Not found, all clear!")
    return 1
if len(sys.argv) == 2 and len(sys.argv[1]) > 0:
    exit(fonk2(sys.argv[1]))
else:
    print("\tUse:\n\t" + os.path.basename(__file__) + " [b2|SHA1]")