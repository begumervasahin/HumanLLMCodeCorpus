import os
import hashlib
import sys
import binascii
import re
from platform import system
PWNED_PASSWORD_FILES = [
    'pwned-passwords-ordered-2.0.bin'
]
HASH_LENGTH = 20
DETECT_HASH = True
VERBOSE = 0
IS_WINDOWS = system() == 'Windows'
def get_file_size(filename):
    try:
        return os.path.getsize(filename)
    except FileNotFoundError:
        if VERBOSE > 0:
            print(f"File not found: {filename}")
        return 0
def normalize_password(password):
    try:
        if IS_WINDOWS:
            return password.decode('cp1252').encode('utf-8')
        return password.decode('utf-8').encode('utf-8')
    except UnicodeDecodeError:
        return password.encode('utf-8')
def calculate_sha1_hash(password):
    return hashlib.sha1(password).hexdigest().upper()
def is_valid_sha1(password):
    return len(password) == HASH_LENGTH * 2 and re.match(r'^[a-fA-F0-9]+$', password)
def search_for_password(password):
    password = normalize_password(password)
    pass_hash = calculate_sha1_hash(password)
    if DETECT_HASH and is_valid_sha1(password.decode('utf-8')):
        pass_hash = password.decode('utf-8').upper()
    if VERBOSE > 0:
        print(f"\nSearching for SHA-1 hash: {pass_hash}")
    for password_file in PWNED_PASSWORD_FILES:
        if VERBOSE > 0:
            print(f"Searching in: {password_file}")
        filesize = get_file_size(password_file)
        if filesize == 0:
            return 1
        num_hashes = filesize
        if VERBOSE > 1:
            print(f"File size: {filesize} bytes, hash length: {HASH_LENGTH} bytes, number of hashes: {num_hashes}")
        pos_from, pos_to = 0, num_hashes
        with open(password_file, "rb") as file:
            while pos_from < pos_to:
                current_pos = (pos_to + pos_from)
                file.seek(current_pos * HASH_LENGTH)
                pwned_hash = binascii.hexlify(file.read(HASH_LENGTH)).upper().decode('utf-8')
                if VERBOSE > 1:
                    print(f"Checking position {current_pos}")
                if pwned_hash == pass_hash:
                    if VERBOSE > 0:
                        print(f"Found: '{password.decode('utf-8')}' as {pwned_hash}")
                    return 0
                if pwned_hash < pass_hash:
                    pos_from = current_pos + 1
                else:
                    pos_to = current_pos
    if VERBOSE > 0:
        print("Not found, all clear!")
    return 1
def main():
    if len(sys.argv) == 2 and sys.argv[1]:
        password_or_hash = sys.argv[1].encode('utf-8')
        sys.exit(search_for_password(password_or_hash))
    else:
        script_name = os.path.basename(__file__)
        print(f"Usage:\n\t{script_name} [password|SHA1]")
if __name__ == "__main__":
    main()