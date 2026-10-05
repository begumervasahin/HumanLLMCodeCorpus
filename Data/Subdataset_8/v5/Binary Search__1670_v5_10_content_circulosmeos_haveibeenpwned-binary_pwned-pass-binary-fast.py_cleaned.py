import os
import sys
import hashlib
import binascii
from re import match
from platform import system
PWNED_PASSWORDS_FILES = ['pwned-passwords-ordered-2.0.bin']
HASH_LENGTH = 20
DETECT_HASH = 1
VERBOSE = 0
WINDOWS = system() == 'Windows'
def get_file_size(filename):
    return os.path.getsize(filename)
def search_for_password(password):
    try:
        password = password.decode('utf-8').encode('utf-8') if not WINDOWS else password.decode('cp1252').encode('utf-8')
    except:
        password = password.encode('utf-8')
    pass_hash = hashlib.sha1(password).hexdigest().upper()
    if DETECT_HASH == 1 and len(password) == HASH_LENGTH * 2 and match(r'^[a-fA-F0-9]+$', password.decode('utf-8')):
        pass_hash = password.decode('utf-8').upper()
    if VERBOSE > 0:
        print("\nSearching for SHA1 hash:", pass_hash)
    for password_file in PWNED_PASSWORDS_FILES:
        if VERBOSE > 0:
            print("Searching in:", password_file)
        try:
            filesize = get_file_size(password_file)
        except:
            if VERBOSE > 0:
                print("File not found:", password_file)
            return 1
        number_of_hashes = filesize
        if VERBOSE > 1:
            print("File size is:", filesize, "bytes, hash length is", HASH_LENGTH, "bytes, number of hashes is", number_of_hashes)
        pos_from, pos_to = 0, number_of_hashes
        with open(password_file, "rb") as file:
            while True:
                current_pos = (pos_to + pos_from)
                file.seek(current_pos * HASH_LENGTH)
                pwned_hash = binascii.hexlify(bytearray(file.read(HASH_LENGTH))).upper().decode('utf-8')
                if pwned_hash == pass_hash:
                    if VERBOSE > 0:
                        print("Found:", password.decode('utf-8'), "as", pwned_hash)
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
    if VERBOSE > 0:
        print("Not found, all clear!")
    return 1
if len(sys.argv) == 2 and len(sys.argv[1]) > 0:
    exit(search_for_password(sys.argv[1]))
else:
    print("\tUse:\n\t" + os.path.basename(__file__) + " [password|SHA1]")