import os
import hashlib
import sys
import binascii
from re import match
from platform import system
PWNED_PASSWORDS_FILES = ['pwned-passwords-ordered-2.0.bin']
HASH_LENGTH = 20
DETECT_HASH = True
VERBOSE = False
WINDOWS = system() == 'Windows'
def get_file_size(filename):
    return os.path.getsize(filename)
def search_for_password(password):
    try:
        if not WINDOWS:
            password = password.decode('utf-8').encode('utf-8')
        else:
            password = password.decode('cp1252').encode('utf-8')
    except AttributeError:
        password = password.encode('utf-8')
    pass_hash = hashlib.sha1(password).hexdigest().upper()
    if DETECT_HASH and len(password) == HASH_LENGTH * 2 and match(r'^[a-fA-F0-9]+$', password.decode('utf-8')):
        pass_hash = password.decode('utf-8').upper()
    if VERBOSE:
        print(f"\nSearching for SHA1 hash: {pass_hash}")
    for password_file in PWNED_PASSWORDS_FILES:
        if VERBOSE:
            print(f"Searching in: {password_file}")
        try:
            filesize = get_file_size(password_file)
        except FileNotFoundError:
            if VERBOSE:
                print(f"File not found: {password_file}")
            return 1
        number_of_hashes = filesize
        if VERBOSE:
            print(f"File size: {filesize} bytes, hash length: {HASH_LENGTH} bytes, number of hashes: {number_of_hashes}")
        pos_from = 0
        pos_to = number_of_hashes
        with open(password_file, "rb") as file:
            while pos_from < pos_to:
                current_pos = (pos_to + pos_from)
                file.seek(current_pos * HASH_LENGTH)
                pwned_hash = binascii.hexlify(file.read(HASH_LENGTH)).upper().decode('utf-8')
                if VERBOSE:
                    print(f"Checking hash position {current_pos}: {pwned_hash}")
                if pwned_hash == pass_hash:
                    if VERBOSE:
                        print(f"Found: '{password.decode('utf-8')}' as {pwned_hash}")
                    return 0
                elif pwned_hash < pass_hash:
                    pos_from = current_pos + 1
                else:
                    pos_to = current_pos
    if VERBOSE:
        print("Not found, all clear!")
    return 1
if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1]:
        sys.exit(search_for_password(sys.argv[1]))
    else:
        print(f"Usage:\n\t{os.path.basename(__file__)} [password|SHA1]")