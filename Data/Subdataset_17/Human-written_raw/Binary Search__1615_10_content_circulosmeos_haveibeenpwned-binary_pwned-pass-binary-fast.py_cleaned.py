import os
import hashlib
import sys
import binascii
from re import match
from platform import system
pwned_passwords_files = [
    'pwned-passwords-ordered-2.0.bin'
]
HASH_LENGTH = 20;
DETECT_HASH = 1
VERBOSE = 0
if (system() == 'Windows'):
    WINDOWS = 1
else:
    WINDOWS = 0
def getFileSize(filename):
    return os.path.getsize(filename)
def searchForPass(password):
    try:
        if (WINDOWS==0):
            password = password.decode('utf-8').encode('utf-8')
        else:
            password = password.decode('cp1252').encode('utf-8')
    except:
        password = password.encode('utf-8')
    pass_hash = hashlib.sha1(password).hexdigest().upper()
    if (DETECT_HASH==1):
        if (len(password)==HASH_LENGTH*2):
            if ( match(r'^[a-fA-F0-9]+$',password.decode('utf-8')) ):
                pass_hash = password.decode('utf-8').upper()
    if (VERBOSE>0): print("\nSearching for SHA1 hash: %s" % pass_hash)
    for password_file in pwned_passwords_files:
        if (VERBOSE>0): print("Searching in: %s" % password_file)
        try:
                filesize = getFileSize(password_file)
        except:
                if (VERBOSE>0): print( "File not found: %s" % password_file )
                return 1
        number_of_hashes = filesize / HASH_LENGTH
        if (VERBOSE>1):
            print("File size is: %s bytes, hash length is %s bytes, number of hashes is %s"
                % (filesize, HASH_LENGTH, number_of_hashes))
        pos_from = 0
        pos_to = number_of_hashes
        with open(password_file, "rb") as file:
            while True:
                current_pos = int ((pos_to + pos_from) / 2)
                file.seek(current_pos * HASH_LENGTH)
                pwned_hash = binascii.hexlify( bytearray( file.read( HASH_LENGTH ) ) ).upper().decode('utf-8')
                if (VERBOSE>1): print("Go to %s hash position
                if pwned_hash == pass_hash:
                    if (VERBOSE>0): print("Found: '%s' as %s" % (password.decode('utf-8'), pwned_hash))
                    return 0
                if abs(pos_to - pos_from) < 1:
                    break
                if pwned_hash < pass_hash:
                    pos_from = current_pos
                    if abs(pos_to - pos_from) <= 1:
                        pos_from = pos_to
                else:
                    pos_to = current_pos
                    if abs(pos_to - pos_from) <= 1:
                        pos_to = pos_from
    if (VERBOSE>0): print("Not found, all clear!")
    return 1
if ( len(sys.argv) == 2 and len(sys.argv[1])>0 ):
    exit (
        searchForPass( sys.argv[1] )
        )
else:
    print ("\tUse:\n\t" + os.path.basename(__file__) + " [password|SHA1]")