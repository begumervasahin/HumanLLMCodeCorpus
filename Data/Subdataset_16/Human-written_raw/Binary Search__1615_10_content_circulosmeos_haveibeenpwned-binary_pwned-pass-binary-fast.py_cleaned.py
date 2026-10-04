import os
import hashlib
import sys
import binascii
from re import match
from platform import system
b1 = [
    'pwned-passwords-ordered-2.0.bin'
]
b2 = 20;
a1 = 1
a2 = 0
if (system() == 'Windows'):
    a3 = 1
else:
    a3 = 0
def fonk1(filename):
    return os.path.getsize(filename)
def fonk2(b3):
    try:
        if (a3 = =0):
            b3 = b3.decode('utf-8').encode('utf-8')
        else:
            b3 = b3.decode('cp1252').encode('utf-8')
    except:
        b3 = b3.encode('utf-8')
    b4 = hashlib.sha1(b3).hexdigest().upper()
    if (a1 = =1):
        if (len(b3)==b2*2):
            if ( match(r'^[a-fA-F0-9]+$',b3.decode('utf-8')) ):
                b4 = b3.decode('utf-8').upper()
    if (a2>0): print("\nSearching for SHA1 hash: %s" % b4)
    for password_file in b1:
        if (a2>0): print("Searching in: %s" % password_file)
        try:
                b5 = fonk1(password_file)
        except:
                if (a2>0): print( "File not found: %s" % password_file )
                return 1
        b6 = b5 / b2
        if (a2>1):
            print("File size is: %s bytes, hash length is %s bytes, number of hashes is %s"
                % (b5, b2, b6))
        a4 = 0
        b7 = b6
        with open(password_file, "rb") as file:
            while True:
                b8 = int ((b7 + a4) / 2)
                file.seek(b8 * b2)
                b9 = binascii.hexlify( bytearray( file.read( b2 ) ) ).upper().decode('utf-8')
                if (a2>1): print("Go to %s hash position
                if b9 = = b4:
                    if (a2>0): print("Found: '%s' as %s" % (b3.decode('utf-8'), b9))
                    return 0
                if abs(b7 - a4) < 1:
                    break
                if b9 < b4:
                    a4 = b8
                    if abs(b7 - a4) <= 1:
                        a4 = b7
                else:
                    b7 = b8
                    if abs(b7 - a4) <= 1:
                        b7 = a4
    if (a2>0): print("Not found, all clear!")
    return 1
if ( len(sys.argv) == 2 and len(sys.argv[1])>0 ):
    exit (
        fonk2( sys.argv[1] )
        )
else:
    print ("\tUse:\n\t" + os.path.basename(__file__) + " [b3|SHA1]")